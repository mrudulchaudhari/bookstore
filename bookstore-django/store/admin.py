from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category')  # Include category in list
    fields = ('title', 'author', 'price', 'category', 'image')  # Include category in form

admin.site.register(Book, BookAdmin)
