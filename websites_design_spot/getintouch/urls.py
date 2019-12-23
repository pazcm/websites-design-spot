from django.conf.urls import url, include
from django.contrib import admin
from .views import contactView, successView

urlpatterns = [
    url(r'^contact/$', contactView, name='contact'),
    url(r'^success/$', successView, name='success'),
]
