from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title
