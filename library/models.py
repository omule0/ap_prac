from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='students_books')
    borrowed_books = models.ManyToManyField(Books, related_name='students_borrowed_books')
    return_date = models.DateField(null=True, blank=True)
    fine = models.IntegerField(default=0)

    def __str__(self):
        return self.name
