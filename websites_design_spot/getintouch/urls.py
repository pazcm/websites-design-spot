from django.conf.urls import url
from django.contrib import admin
from .views import contact, success

urlpatterns = [
    url(r'^$', contact, name='contact'),
    url(r'^$', success, name='success'),
]
