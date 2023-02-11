
from graphene_django import DjangoObjectType
from books.models import Books

class DetailsType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("title","author")
