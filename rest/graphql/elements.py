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