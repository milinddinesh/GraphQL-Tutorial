# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from books.models import Books
from .factories import UserFactory

NUM_AUTHORS = 50
NUM_BOOKS = 2

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Books]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the authors
        authors = []
        for _ in range(NUM_AUTHORS):
            person = UserFactory()
            authors.append(person)

