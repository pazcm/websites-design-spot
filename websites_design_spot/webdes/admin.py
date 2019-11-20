from django.contrib import admin
from .models import Webdes, Category

# Add websites through admin panel
admin.site.register(Webdes)
admin.site.register(Category)
