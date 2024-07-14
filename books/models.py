from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()

