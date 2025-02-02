import graphene
from graphene import ObjectType, Float, Field, Dict


class StoichiometryInput(graphene.InputObjectType):
    reactants = graphene.JSONString()
    products = graphene.JSONString()


class StoichiometryResultType(ObjectType):
    molar_ratio = graphene.JSONString()


class PHCalculatorInput(graphene.InputObjectType):
    concentration_of_hplus = Float()


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


class CalculateStoichiometry(graphene.Mutation):
    class Arguments:
        input = StoichiometryInput(required=True)

    Output = StoichiometryResultType

    def mutate(self, info, input):
        reactants = input.reactants
        products = input.products

        molar_ratio = {key: value / reactants[key] for key, value in products.items()}
        return StoichiometryResultType(molar_ratio=molar_ratio)


class CalculatePH(graphene.Mutation):
    class Arguments:
        input = PHCalculatorInput(required=True)

    Output = PHCalculatorResultType

    def mutate(self, info, input):
        concentration_of_hplus = input.concentration_of_hplus
        ph = -1 * (concentration_of_hplus ** -1)
        return PHCalculatorResultType(ph=ph)


class CalculateIdealGasLaw(graphene.Mutation):
    class Arguments:
        input = IdealGasLawInput(required=True)

    Output = IdealGasLawResultType

    def mutate(self, info, input):
        pressure = input.pressure
        volume = input.volume
        temperature = input.temperature

        n = (pressure * volume) / (0.0821 * temperature)  # Menggunakan konstanta gas ideal
        return IdealGasLawResultType(n=n)


class Mutation(ObjectType):
    calculate_stoichiometry = CalculateStoichiometry.Field()
    calculate_ph = CalculatePH.Field()
    calculate_ideal_gas_law = CalculateIdealGasLaw.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
