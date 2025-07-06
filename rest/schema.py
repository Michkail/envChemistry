import math
import re
import graphene
from graphene import ObjectType, Float, String, List
from graphene.types.generic import GenericScalar
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


class ElementListResponse(graphene.ObjectType):
    message = graphene.String()
    data = graphene.List(ElementType)


class StoichiometryExtendedInput(graphene.InputObjectType):
    reactants = GenericScalar()
    products = GenericScalar()


class PHInput(graphene.InputObjectType):
    concentration = Float()


class GasLawInput(graphene.InputObjectType):
    pressure = Float()
    volume = Float()
    temperature = Float()


class VanDerWaalsInput(graphene.InputObjectType):
    pressure = Float()
    volume = Float()
    moles = Float()
    temperature = Float()
    const_a = Float()
    const_b = Float()


class EquilibriumInput(graphene.InputObjectType):
    products = List(List(Float))  # [(conc, coef)]
    reactants = List(List(Float))
    temperature = Float()


class GibbsInput(graphene.InputObjectType):
    delta_h = Float()
    delta_s = Float()
    temperature = Float()


class CellPotentialInput(graphene.InputObjectType):
    e_cathode = Float()
    e_anode = Float()


class RateLawInput(graphene.InputObjectType):
    rate_constant = Float()
    concentrations = List(List(Float))  # [(conc, order)]


class HenryLawInput(graphene.InputObjectType):
    henry_constant = Float()
    gas_pressure = Float()


class TitrationInput(graphene.InputObjectType):
    acid_morality = Float()
    acid_volume = Float()
    base_molarity = Float()


class RaoultInput(graphene.InputObjectType):
    pure_pressure = Float()
    solute_fraction = Float()


class EnthalpyInput(graphene.InputObjectType):
    heat = Float()
    temperature = Float()


class BufferInput(graphene.InputObjectType):
    pka = Float()
    acid_concentration = Float()
    base_concentration = Float()


class HessLawInput(graphene.InputObjectType):
    reactants = List(Float)
    products = List(Float)


class NernstInput(graphene.InputObjectType):
    eo = Float()
    n = Float()
    q = Float()


class FreezingBoilingInput(graphene.InputObjectType):
    kf = Float()
    kb = Float()
    m = Float()
    i = Float()


class MoleFractionInput(graphene.InputObjectType):
    na = Float()
    nb = Float()


class HalfLifeInput(graphene.InputObjectType):
    k = Float()


class HeatCapacityInput(graphene.InputObjectType):
    m = Float()
    c = Float()
    delta_t = Float()


class GasDiffusionInput(graphene.InputObjectType):
    m1 = Float()
    m2 = Float()
    r2 = Float()


class MolarMassInput(graphene.InputObjectType):
    formula = String()


class StoichiometryInput(graphene.InputObjectType):
    reactants = graphene.JSONString()
    products = graphene.JSONString()


class PHCalculatorInput(graphene.InputObjectType):
    concentration = Float()


class IdealGasLawInput(graphene.InputObjectType):
    pressure = Float()
    volume = Float()
    temperature = Float()


class ElementType(graphene.ObjectType):
    atomic_number = graphene.Int()
    atomic_mass = graphene.Float()
    symbol = graphene.String()
    name = graphene.String()
    category = graphene.String()
    density = graphene.Float()
    melting_point = graphene.Float()
    boiling_point = graphene.Float()


class GenericSuccessResult(graphene.ObjectType):
    message = String()
    data = GenericScalar()


class Query(ObjectType):
    hello = graphene.String(default_value="Chemical Calculator GraphQL API!")


class GetElementList(graphene.Mutation):
    class Arguments:
        pass

    Output = GenericSuccessResult

    def mutate(self, info):
        elements = Element.objects.all()
        data = [
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

        return GenericSuccessResult(message="Success", data=data)


class CalculateMolarMass(graphene.Mutation):
    class Arguments:
        input = MolarMassInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        formula = input.formula
        elements = {element.symbol: element.atomic_mass for element in Element.objects.all()}
        element_counts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
        total_mass = 0.0

        for element, count in element_counts:
            count = int(count) if count else 1

            if element in elements:
                total_mass += elements[element] * count

            else:
                return GenericSuccessResult(message=f"Element {element} not found", data=None)

        return GenericSuccessResult(message="Success", data={formula: total_mass})


class CalculateStoichiometry(graphene.Mutation):
    class Arguments:
        input = StoichiometryInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        reactants = input.reactants
        products = input.products
        molar_ratio = {
            product: {
                reactant: products[product] / reactants[reactant] for reactant in reactants
            } for product in products
        }

        return GenericSuccessResult(message="Success", data={"molar_ratio": molar_ratio})


class CalculatePH(graphene.Mutation):
    class Arguments:
        input = PHCalculatorInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        concentration = input.concentration
        ph = -math.log10(concentration)
        poh = 14 - ph

        return GenericSuccessResult(message="Success", data={"pH": ph, "pOH": poh})


class CalculateIdealGasLaw(graphene.Mutation):
    class Arguments:
        input = IdealGasLawInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        pressure = input.pressure
        volume = input.volume
        temperature = input.temperature
        n = (pressure * volume) / (0.0821 * temperature)

        return GenericSuccessResult(message="Success", data={"n": n})
    

class CalculatePHGraphQL(graphene.Mutation):
    class Arguments:
        input = PHInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        ph = -math.log10(input.concentration)
        poh = 14 - ph

        return GenericSuccessResult(message="Success", data={"pH": ph, "pOH": poh})


class CalculateGasLaw(graphene.Mutation):
    class Arguments:
        input = GasLawInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        n = (input.pressure * input.volume) / (0.0821 * input.temperature)

        return GenericSuccessResult(message="Success", data={"n": n})


class CalculateVanDerWaals(graphene.Mutation):
    class Arguments:
        input = VanDerWaalsInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        r = 0.0821
        try:
            corrected = ((input.moles * r * input.temperature) / (input.volume - input.moles * input.const_b)) - (input.const_a * input.moles ** 2 / input.volume ** 2)
        
        except ZeroDivisionError:
            return GenericSuccessResult(message="Invalid input: division by zero", data=None)
        
        return GenericSuccessResult(message="Success", data={"corrected_pressure": corrected})


class CalculateEquilibrium(graphene.Mutation):
    class Arguments:
        input = EquilibriumInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        kc = math.prod([c ** co for c, co in input.products]) / math.prod([c ** co for c, co in input.reactants])
        return GenericSuccessResult(message="Success", data={"Kc": kc})


class CalculateGibbs(graphene.Mutation):
    class Arguments:
        input = GibbsInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        delta_g = input.delta_h - (input.temperature * input.delta_s / 1000)
        spontaneity = "Spontaneous" if delta_g < 0 else "Non-spontaneous"
        return GenericSuccessResult(message="Success", data={"Gibbs_free_energy": delta_g, "reaction": spontaneity})


class CalculateCellPotential(graphene.Mutation):
    class Arguments:
        input = CellPotentialInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        e_cell = input.e_cathode - input.e_anode
        return GenericSuccessResult(message="Success", data={"cell_potential": e_cell})


class CalculateRateLaw(graphene.Mutation):
    class Arguments:
        input = RateLawInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        rate = input.rate_constant * math.prod([c ** o for c, o in input.concentrations])
        return GenericSuccessResult(message="Success", data={"reaction_rate": rate})


class CalculateHenry(graphene.Mutation):
    class Arguments:
        input = HenryLawInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        concentration = input.henry_constant * input.gas_pressure
        return GenericSuccessResult(message="Success", data={"gas_solubility": concentration})


class CalculateTitration(graphene.Mutation):
    class Arguments:
        input = TitrationInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        v2 = (input.acid_morality * input.acid_volume) / input.base_molarity
        return GenericSuccessResult(message="Success", data={"equivalence_volume": v2})


class CalculateRaoult(graphene.Mutation):
    class Arguments:
        input = RaoultInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        vapor_pressure = input.pure_pressure * (1 - input.solute_fraction)
        return GenericSuccessResult(message="Success", data={"vapor_pressure_solution": vapor_pressure})


class CalculateEnthalpy(graphene.Mutation):
    class Arguments:
        input = EnthalpyInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        entropy = input.heat / input.temperature
        return GenericSuccessResult(message="Success", data={"entropy_change": entropy})


class CalculateBufferPH(graphene.Mutation):
    class Arguments:
        input = BufferInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        ph = input.pka + math.log10(input.base_concentration / input.acid_concentration)
        return GenericSuccessResult(message="Success", data={"buffer_pH": ph})


class CalculateHessLaw(graphene.Mutation):
    class Arguments:
        input = HessLawInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        delta_h = sum(input.products) - sum(input.reactants)
        return GenericSuccessResult(message="Success", data={"delta_h": delta_h})


class CalculateNernst(graphene.Mutation):
    class Arguments:
        input = NernstInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        e = input.eo - (0.0591 / input.n) * math.log10(input.q)
        return GenericSuccessResult(message="Success", data={"E": e})


class CalculateFreezingBoiling(graphene.Mutation):
    class Arguments:
        input = FreezingBoilingInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        delta_tf = input.i * input.kf * input.m
        delta_tb = input.i * input.kb * input.m
        return GenericSuccessResult(message="Success", data={"delta_Tf": delta_tf, "delta_Tb": delta_tb})


class CalculateMoleFraction(graphene.Mutation):
    class Arguments:
        input = MoleFractionInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        total = input.na + input.nb
        xa = input.na / total if total else 0
        xb = input.nb / total if total else 0
        return GenericSuccessResult(message="Success", data={"xA": xa, "xB": xb})


class CalculateHalfLife(graphene.Mutation):
    class Arguments:
        input = HalfLifeInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        half_life = 0.693 / input.k
        return GenericSuccessResult(message="Success", data={"half_life": half_life})


class CalculateHeatCapacity(graphene.Mutation):
    class Arguments:
        input = HeatCapacityInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        q = input.m * input.c * input.delta_t
        return GenericSuccessResult(message="Success", data={"q": q})


class CalculateGasDiffusion(graphene.Mutation):
    class Arguments:
        input = GasDiffusionInput(required=True)

    Output = GenericSuccessResult

    def mutate(self, info, input):
        r1 = input.r2 * math.sqrt(input.m2 / input.m1)
        return GenericSuccessResult(message="Success", data={"r1": r1})


class Mutation(ObjectType):
    getElementList = GetElementList.Field()
    calculate_molar_mass = CalculateMolarMass.Field()
    calculate_stoichiometry = CalculateStoichiometry.Field()
    calculate_ph = CalculatePH.Field()
    calculate_ideal_gas_law = CalculateIdealGasLaw.Field()
    calculate_ph_accurate = CalculatePHGraphQL.Field()
    calculate_gas_law = CalculateGasLaw.Field()
    calculate_van_der_waals = CalculateVanDerWaals.Field()
    calculate_equilibrium = CalculateEquilibrium.Field()
    calculate_gibbs = CalculateGibbs.Field()
    calculate_cell_potential = CalculateCellPotential.Field()
    calculate_rate_law = CalculateRateLaw.Field()
    calculate_henry = CalculateHenry.Field()
    calculate_titration = CalculateTitration.Field()
    calculate_raoult = CalculateRaoult.Field()
    calculate_entropy = CalculateEnthalpy.Field()
    calculate_buffer_ph = CalculateBufferPH.Field()
    calculate_hess_law = CalculateHessLaw.Field()
    calculate_nernst = CalculateNernst.Field()
    calculate_freezing_boiling = CalculateFreezingBoiling.Field()
    calculate_mole_fraction = CalculateMoleFraction.Field()
    calculate_half_life = CalculateHalfLife.Field()
    calculate_heat_capacity = CalculateHeatCapacity.Field()
    calculate_gas_diffusion = CalculateGasDiffusion.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
