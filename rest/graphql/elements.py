import graphene


class IsotopeType(graphene.ObjectType):
    symbol = graphene.String()
    mass = graphene.Float()
    abundance = graphene.Float()
    half_life = graphene.String()
    decay_mode = graphene.String()


class ElementType(graphene.ObjectType):
    atomic_number = graphene.Int()
    atomic_mass = graphene.Float()
    atomic_radius = graphene.Float()
    covalent_radius = graphene.Float()
    van_der_waals_radius = graphene.Float()
    symbol = graphene.String()
    name = graphene.String()
    category = graphene.String()
    period = graphene.Int()
    group = graphene.Int()
    block = graphene.String()
    phase = graphene.String()
    density = graphene.Float()
    melting_point = graphene.Float()
    boiling_point = graphene.Float()
    electron_configuration = graphene.String()
    electronegativity = graphene.Float()
    electron_affinity = graphene.Float()
    electrical_conductivity = graphene.Float()
    thermal_conductivity = graphene.Float()
    ionization_energy = graphene.Float()
    isotopes = graphene.List(IsotopeType)
    oxidation_state = graphene.List(graphene.Int)
    abundance_earth_crust = graphene.Float()
    abundance_universe = graphene.Float()
    specific_heat = graphene.Float()
    appearance = graphene.String()
    crystal_structure = graphene.String()
    discovery_year = graphene.Int()
    discovery_by = graphene.String()


class ElementListResponse(graphene.ObjectType):
    message = graphene.String()
    data = graphene.List(ElementType)


class CompoundType(graphene.ObjectType):
    name = graphene.String()
    chemical_formula = graphene.String()
    category = graphene.String()
    bond_type = graphene.String()
    properties = graphene.String()
    uses = graphene.String()
    status = graphene.String()
    discovery_date = graphene.String()
    discovery_period = graphene.String()
    discovery_by = graphene.String()
    source = graphene.String()


class CompoundListResponse(graphene.ObjectType):
    message = graphene.String()
    data = graphene.List(CompoundType)
