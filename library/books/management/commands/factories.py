import factory 
from factory.django import DjangoModelFactory

from books.models import Books

# Defining a factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = Books

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')


u = UserFactory()
u.title
u.author