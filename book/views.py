from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from . import form
from django.http import HttpResponse


# Create your views here.
def book_1(request):
    books = models.Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_2(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'about.html', {'book': book})


def add_book(request):
    method = request.method
    if method == 'POST':
        forms = form.BookForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponse('Book created')
    else:
        forms = form.BookForm()
    return render(request, 'add_book.html', {'forms': forms})


