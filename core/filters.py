import django_filters
from core.models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        #fields=['name','author__name','price','genre'] #search exact value only

        #search method 2
        fields={'name':['icontains'],
                'author__name':['icontains'],
                'price':['lt','gt'],
                'genre':['exact']
                }

