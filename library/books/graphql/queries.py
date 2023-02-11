# Here lies all the queries 

import graphene
from books.graphql.types import DetailsType
from books.models import Books


class Query(graphene.ObjectType):
    all_authors = graphene.List(DetailsType)

    def resolve_all_authors(root, info):
        return Books.objects.all()
        # return Ingredient.objects.select_related("category").all()


#modify the queries so that we can get all details about the book . 