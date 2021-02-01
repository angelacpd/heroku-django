import graphene


class ItemInput(graphene.InputObjectType):
    item_text = graphene.String()
    item_group = graphene.String()
