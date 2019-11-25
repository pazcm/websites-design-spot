from django.conf.urls import url, include
from .views import all_webdes, WebdesDetail, webdes_category
from .views import webdes_home

urlpatterns = [
    url(r'^$', all_webdes, name='webdes'),
    url(r'^(?P<pk>\d+)/$', WebdesDetail.as_view(), name='webdes-detail'),
    url(r'^$',  webdes_home, name='index'),
    url(r'^$',  webdes_category, name='category'),
]
