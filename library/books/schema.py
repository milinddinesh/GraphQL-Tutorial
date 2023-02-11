import graphene
from  books.graphql.queries import Query
schema = graphene.Schema(query=Query)
