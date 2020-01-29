from django.conf.urls import url, include
from .views import all_webdes, WebdesDetail, filter_webdes
from .views import webdes_home

urlpatterns = [
    url(r'^$', all_webdes, name='webdes'),
    url(r'^(?P<pk>\d+)/$', WebdesDetail.as_view(), name='webdes-detail'),
    url(r'^$',  webdes_home, name='index'),
    url(r'^(?P<requestedCategory>[a-zA-Z ]*)$', filter_webdes, name='filter_webdes'),
]
