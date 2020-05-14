import graphene
import Polls.polls.schema


class Query(Polls.polls.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(Polls.polls.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
