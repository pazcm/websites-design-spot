from django.shortcuts import render
from .models import Webdes

# Create your views here

def all_webdes(request):
    webdes = Webdes.objects.all()
    return render(request, "webdes.html", {"webdes": webdes})
