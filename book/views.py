from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


# Create your views here.
def book_1(request):
    books = models.Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_2(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'about.html', {'book': book})
