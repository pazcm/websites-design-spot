"""websites_design_spot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from account import urls as urls_account
from webdes import urls as urls_webdes
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from getintouch import urls as urls_getintouch
from getintouch import urls as urls_contact
from getintouch import urls as urls_success
# from getintouch.views import success
from webdes.views import all_webdes
from webdes.views import webdes_home
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', all_webdes, name='index'),
    url(r'^$', webdes_home, name='index'),
    url(r'^account/', include(urls_account)),
    url(r'^webdes/', include(urls_webdes)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^getintouch/', include(urls_getintouch)),
     url(r'^contact/', include(urls_contact)),
    url(r'^success/', include(urls_success)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
