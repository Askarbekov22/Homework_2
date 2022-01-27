from django.forms import forms
from . import parser, parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('FILM', 'FILM'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'FILM':
            film_parser = parser.parser()
            for i in film_parser:
                models.Film.objects.create(**i)
