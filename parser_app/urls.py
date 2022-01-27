from django.urls import path
from . import views

urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name="parser"),
    path('parser/list/films', views.ParserListView.as_view(), name='parserlistfilms'),
    path('parser/list/films/<int:id>', views.FilmDetailView.as_view(), name="film_d")
]
