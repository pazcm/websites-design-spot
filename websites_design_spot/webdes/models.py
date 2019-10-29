from django.db import models

# Create your models here.

# It will create the database for the 'webdes' / provisinal model

class Webdes(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    # category = models.CharField(max_length=100)  # reference field ?
   
    def __str__(self):
        return self.name