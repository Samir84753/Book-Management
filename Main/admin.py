from django.contrib import admin
from .models import Books
# Register your models here.
class books_display(admin.ModelAdmin):
    list_display=('name','isbn')

admin.site.register(Books,books_display)
