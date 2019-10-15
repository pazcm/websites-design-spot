from django.db import models

# Create your models here.

# It will create the database for the 'webdes'
class Webdes(models.Model):
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    category = models.CharField(max_length=100)  # reference field ?
    price = models.DecimalField(
        max_digits=6, decimal_places=2)  # price field ?

    def __str__(self):
        return self.name
