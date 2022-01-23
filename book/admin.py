from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Book)
admin.site.register(models.BooksComment)
admin.site.register(models.ExpertRecomendation)
admin.site.register(models.Expert)