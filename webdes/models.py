from django.db import models

# Create your models here

# It will create the database for the 'webdes'

class Webdes(models.Model):
    # It will add 'category' field to the db
    CATEGORY_CHOICES = [
        ('P', 'Professional'),
        ('E', 'Event'),
        ('A', 'Abastract'),
        ('EC', 'Ecommerce'),
        ('NP', 'Non-Profit'),
    ]

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, default='Event')
   
    def __str__(self):
        return self.name
