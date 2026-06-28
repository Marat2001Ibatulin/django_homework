import json
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(r'C:\Users\Marat\IdeaProjects\dj-homeworks\2.1-databases\models_list_displaying\fixtures\books.json',
                  encoding='UTF-8') as file:
            books = json.load(file)

        for book in books:
            Book(name=book['fields']['name'], author=book['fields']['author'],
                 pub_date=book['fields']['pub_date']).save()