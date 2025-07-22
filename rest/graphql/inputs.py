import graphene

class CompoundInput(graphene.InputObjectType):
    formula = graphene.String()
    coefficient = graphene.Float()


class IsotopeInput(graphene.InputObjectType):
    symbol = graphene.String(required=True)
    mass = graphene.Float()
    abundance = graphene.Float()
    half_life = graphene.String()
    decay_mode = graphene.String()


class ElementUpdateInput(graphene.InputObjectType):
    atomic_number = graphene.Int(required=True)
    atomic_mass = graphene.Decimal()
    atomic_radius = graphene.Decimal()
    covalent_radius = graphene.Decimal()
    van_der_waals_radius = graphene.Decimal()
    symbol = graphene.String()
    name = graphene.String()
    category = graphene.String()
    period = graphene.Int()
    group = graphene.Int()
    block = graphene.String()
    phase = graphene.String()
    density = graphene.Decimal()
    melting_point = graphene.Decimal()
    boiling_point = graphene.Decimal()
    electron_configuration = graphene.String()
    electronegativity = graphene.Decimal()
    electron_affinity = graphene.Decimal()
    electrical_conductivity = graphene.Decimal()
    thermal_conductivity = graphene.Decimal()
    ionization_energy = graphene.Decimal()
    oxidation_state = graphene.List(graphene.Int)
    abundance_earth_crust = graphene.Decimal()
    abundance_universe = graphene.Decimal()
    specific_heat = graphene.Decimal()
    appearance = graphene.String()
    crystal_structure = graphene.String()
    discovery_year = graphene.Int()
    discovery_by = graphene.String()
    isotopes = graphene.List(IsotopeInput)


class ConcentrationInput(graphene.InputObjectType):
    value = graphene.Float()
    order = graphene.Float()


class StoichiometryInput(graphene.InputObjectType):
    reactants = graphene.List(CompoundInput)
    products = graphene.List(CompoundInput)


class PHInput(graphene.InputObjectType):
    concentration = graphene.Float()
    pka = graphene.Float(required=True)


class VanDerWaalsInput(graphene.InputObjectType):
    pressure = graphene.Float()
    volume = graphene.Float()
    moles = graphene.Float()
    temperature = graphene.Float()
    const_a = graphene.Float()
    const_b = graphene.Float()


class EquilibriumInput(graphene.InputObjectType):
    products = graphene.List(ConcentrationInput)
    reactants = graphene.List(ConcentrationInput)
    temperature = graphene.Float()


class GibbsInput(graphene.InputObjectType):
    delta_h = graphene.Float()
    delta_s = graphene.Float()
    temperature = graphene.Float()


class CellPotentialInput(graphene.InputObjectType):
    e_cathode = graphene.Float()
    e_anode = graphene.Float()


class RateLawInput(graphene.InputObjectType):
    rate_constant = graphene.Float()
    concentrations = graphene.List(ConcentrationInput)


class HenryLawInput(graphene.InputObjectType):
    henry_constant = graphene.Float()
    gas_pressure = graphene.Float()


class TitrationInput(graphene.InputObjectType):
    acid_morality = graphene.Float()
    acid_volume = graphene.Float()
    base_molarity = graphene.Float()


class RaoultInput(graphene.InputObjectType):
    pure_pressure = graphene.Float()
    solute_fraction = graphene.Float()


class EnthalpyInput(graphene.InputObjectType):
    heat = graphene.Float()
    temperature = graphene.Float()


class BufferInput(graphene.InputObjectType):
    pka = graphene.Float()
    acid_concentration = graphene.Float()
    base_concentration = graphene.Float()


class HessLawInput(graphene.InputObjectType):
    reactants = graphene.List(graphene.Float)
    products = graphene.List(graphene.Float)


class NernstInput(graphene.InputObjectType):
    eo = graphene.Float()
    n = graphene.Float()
    q = graphene.Float()


class FreezingBoilingInput(graphene.InputObjectType):
    kf = graphene.Float()
    kb = graphene.Float()
    m = graphene.Float()
    i = graphene.Float()


class MoleFractionInput(graphene.InputObjectType):
    na = graphene.Float()
    nb = graphene.Float()


class HalfLifeInput(graphene.InputObjectType):
    k = graphene.Float()


class HeatCapacityInput(graphene.InputObjectType):
    m = graphene.Float()
    c = graphene.Float()
    delta_t = graphene.Float()


class GasDiffusionInput(graphene.InputObjectType):
    m1 = graphene.Float()
    m2 = graphene.Float()
    r2 = graphene.Float()


class MolarMassInput(graphene.InputObjectType):
    formula = graphene.String()