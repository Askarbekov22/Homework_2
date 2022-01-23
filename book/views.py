from django.shortcuts import render, redirect
from . import models
from django.shortcuts import get_object_or_404
from . import forms
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic


class BooksListView(generic.ListView):
    template_name = 'index.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.filter().order_by("-id")


# Create your views here.
# def book_1(request):
#   books = models.Book.objects.all()
#  return render(request, "index.html", {"books": books})


# def book_2(request, id):
#   book = get_object_or_404(models.Book, id=id)
#  return render(request, 'about.html', {'book': book})
class BooksDetailView(generic.DetailView):
    template_name = 'about.html'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)


# def add_book(request):
#   method = request.method
#  if method == 'POST':
#     form = forms.BookForm(request.POST, request.FILES)
#    if form.is_valid():
#       form.save()
#      return HttpResponse('Book created')
# else:
#   form = forms.BookForm()
# return render(request, 'add_book.html', {'form': form})

class BooksCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)


# def book_update(request, id):
#   book_object = get_object_or_404(models.Book, id=id)
#  if request.method == 'POST':
#     form = forms.BookForm(instance=book_object, data=request.POST)
#    if form.is_valid():
#       form.save()
#      # return HttpResponse('Book Updated Successfully')
#     return redirect(reverse("books:book"))

# else:
#   form = forms.BookForm(instance=book_object)
# return render(request, 'book_update.html', {'form': form, 'object': book_object})
class BooksUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)

    def form_valid(self, form):
        return super(BooksUpdateView, self).form_valid(form=form)


# def book_delete(request, id):
# book_object = get_object_or_404(models.Book, id=id)
# book_object.delete()
# return HttpResponse('Book Deleted')
class BooksDeleteView(generic.DeleteView):
    template_name = 'confirm_delete_book.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)
