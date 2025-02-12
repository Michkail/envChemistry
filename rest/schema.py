import re
import graphene
from graphene import ObjectType, Float, Field, String
from rest.models import Element


class ElementType(graphene.ObjectType):
    atomic_number = graphene.Int()
    atomic_mass = graphene.Float()
    symbol = graphene.String()
    name = graphene.String()
    category = graphene.String()
    density = graphene.Float()
    melting_point = graphene.Float()
    boiling_point = graphene.Float()


class MolarMassInput(graphene.InputObjectType):
    formula = String()


class MolarMassResultType(ObjectType):
    molar_mass = graphene.JSONString()


class StoichiometryInput(graphene.InputObjectType):
    reactants = graphene.JSONString()
    products = graphene.JSONString()


class StoichiometryResultType(ObjectType):
    molar_ratio = graphene.JSONString()


class PHCalculatorInput(graphene.InputObjectType):
    concentration = Float()


class PHCalculatorResultType(ObjectType):
    ph = Float()


class IdealGasLawInput(graphene.InputObjectType):
    pressure = Float()
    volume = Float()
    temperature = Float()


class IdealGasLawResultType(ObjectType):
    n = Float()


class Query(ObjectType):
    hello = graphene.String(default_value="Chemical Calculator GraphQL API!")


class GetElementList(graphene.Mutation):
    class Arguments:
        pass

    Output = graphene.List(ElementType)

    def mutate(self, info):
        elements = Element.objects.all()
        return [
            {
                "atomic_number": e.atomic_number,
                "atomic_mass": e.atomic_mass,
                "symbol": e.symbol,
                "name": e.name,
                "category": e.category,
                "density": e.density,
                "melting_point": e.melting_point,
                "boiling_point": e.boiling_point
            } for e in elements
        ]


class CalculateMolarMass(graphene.Mutation):
    class Arguments:
        input = MolarMassInput(required=True)

    Output = MolarMassResultType

    def mutate(self, info, input):
        formula = input.formula
        elements = {element.symbol: element.atomic_mass for element in Element.objects.all()}
        element_counts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
        total_mass = 0.0

        for element, count in element_counts:
            count = int(count) if count else 1

            if element in elements:
                total_mass += elements[element] * count

        return MolarMassResultType(molar_mass={formula: total_mass})


class CalculateStoichiometry(graphene.Mutation):
    class Arguments:
        input = StoichiometryInput(required=True)

    Output = StoichiometryResultType

    def mutate(self, info, input):
        reactants = input.reactants
        products = input.products
        molar_ratio = {
            product: {
                reactant: products[product] / reactants[reactant] for reactant in reactants
            } for product in products
        }

        return StoichiometryResultType(molar_ratio=molar_ratio)


class CalculatePH(graphene.Mutation):
    class Arguments:
        input = PHCalculatorInput(required=True)

    Output = PHCalculatorResultType

    def mutate(self, info, input):
        concentration = input.concentration
        ph = -1 * (concentration ** -1)

        return PHCalculatorResultType(ph=ph)


class CalculateIdealGasLaw(graphene.Mutation):
    class Arguments:
        input = IdealGasLawInput(required=True)

    Output = IdealGasLawResultType

    def mutate(self, info, input):
        pressure = input.pressure
        volume = input.volume
        temperature = input.temperature
        n = (pressure * volume) / (0.0821 * temperature)

        return IdealGasLawResultType(n=n)


class Mutation(ObjectType):
    getElementList = GetElementList.Field()
    calculate_molar_mass = CalculateMolarMass.Field()
    calculate_stoichiometry = CalculateStoichiometry.Field()
    calculate_ph = CalculatePH.Field()
    calculate_ideal_gas_law = CalculateIdealGasLaw.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
