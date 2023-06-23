from django.shortcuts import render

from .forms import BookNameFilterForm
from .models import Book
from core.filters import BookFilter

# Create your views here.

def index(request):
    ##normal search filter
    #name = request.GET.get('name')
    #form = BookNameFilterForm()
    #books = Book.objects.all()

    #if name:
     #   books = books.filter(name__icontains=name)
    ##normal search filter

    books = Book.objects.all()
    
    book_filter = BookFilter(request.GET,queryset=books)
    
     
    context={'form':book_filter.form,'books':book_filter.qs}
    return render(request,'core/index.html',context)
