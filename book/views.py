from django.shortcuts import render, redirect
from . import models
from django.shortcuts import get_object_or_404
from . import forms
from django.http import HttpResponse
from django.urls import reverse


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
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})


def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Book Updated Successfully')
            return redirect(reverse("books:book"))

    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form, 'object': book_object})


def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('Book Deleted')
