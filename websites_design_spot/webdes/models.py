from django.db import models

# Create your models here

# It will add 'category' field to the db

class Category(models.Model):
    title = models.CharField(max_length=40, default='')

# It will create the database for the 'webdes'

class Webdes(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    categories = models.ManyToManyField('Category', related_name='webdes')
   
    def __str__(self):
        return self.name