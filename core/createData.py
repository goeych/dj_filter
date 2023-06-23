from django.core.management.base import BaseCommand
from core.models import Book,Author

class Command(BaseCommand):
    help = 'Load book data'

    def handle(self,*args,**kwargs):
        #create authours
        orwell = Author.objects.get_or_create(name='George Orwell')[0]

        #create books
        Book.objects.get_or_create(
            name='1981',
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4
            )
