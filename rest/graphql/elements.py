import graphene


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
