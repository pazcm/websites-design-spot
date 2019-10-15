from django.conf.urls import url, include
from .views import all_webdes

urlpatterns = [
    url(r'^$', all_webdes, name='webdes'),
]
