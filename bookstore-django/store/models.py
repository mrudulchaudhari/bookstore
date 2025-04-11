
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True) 
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)  # ← Add this

    def __str__(self):
        return self.title
from django.db import models


