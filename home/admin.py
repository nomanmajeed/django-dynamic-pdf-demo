from django.contrib import admin

from .models import Student, Category, Book

# Register your models here.
admin.site.register((Student, Category, Book))
