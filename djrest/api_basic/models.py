from django.db import models
from django.forms import DateField, DateTimeField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    datetime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-datetime',)
    

