import graphene
import pages.schema


class Query(pages.schema.Query, graphene.ObjectType):
    ...


class Mutation(pages.schema.Mutation, graphene.ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
