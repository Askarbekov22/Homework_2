
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView
from . import parser, models, forms


class ParserFormView(FormView):
    template_name = 'parser/parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return redirect(reverse("parserlistfilms"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


class ParserListView(ListView):
    template_name = "parser/index.html"
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return super().get_queryset()


class FilmDetailView(DetailView):
    template_name = 'parser/about_film.html'

    def get_object(self, *kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.Film, id=id)