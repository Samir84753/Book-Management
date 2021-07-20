from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=50)
    isbn=models.CharField(max_length=13,validators=[RegexValidator(regex='(^.{10}$)|(^.{13}$)', message='Isbn has to be either 10 or 13 digits.', code='length_error')],primary_key = True,help_text='ISBN number is 10 or 13 digits.')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f"{self.name}, {self.isbn}"