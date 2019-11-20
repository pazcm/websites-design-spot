from django.conf.urls import url, include
from .views import all_webdes, webdes_category
from .views import webdes_home

urlpatterns = [
    url(r'^$', all_webdes, name='webdes'),
    url(r'^$',  webdes_home, name='index'),
    url(r'^$',  webdes_category, name='category'),
]
