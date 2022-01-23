from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BooksComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.books.title


class Expert(models.Model):
    name=models.CharField(max_length=50,null=True)
    JOB_EXPERT = (
        ("Proger", "Proger"),
        ("Юморист", "Юморист"),
        ("Электрик", "Электрик"),
        ("Дипломат", "Дипломат"),
        ("Таксист", "Таксист"),
        ("Анимешник", "Анимешник"),)
    job_expert = models.CharField(choices=JOB_EXPERT, max_length=100)
    info_about_expert = models.TextField(max_length=200)

    def __str__(self):
        return self.job_expert


class ExpertRecomendation(models.Model):
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, related_name="Expert_Recomendation"
    )

    recomendation_book = models.TextField(max_length=250)
    created_date_expert = models.DateField(auto_now=True)
    expert = models.ForeignKey(
        Expert, on_delete=models.CASCADE, related_name="book_expert"
    )
