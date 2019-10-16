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
from account.views import index, logout, login, register
from account import urls as urls_account
from webdes import urls as urls_webdes
from webdes.views import all_webdes
from django.views import static
from .settings import MEDIA_ROOT
from cart import urls as urls_cart

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_webdes, name='index'),
    url(r'^account/', include(urls_account)),
    url(r'^webdes/', include(urls_webdes)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
