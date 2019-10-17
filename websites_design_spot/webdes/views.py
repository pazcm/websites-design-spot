from django.shortcuts import render
from .models import Webdes

# Create your views here

def all_webdes(request):
    """Return all webdes in the DB and display webdes page"""

    webdes = Webdes.objects.all()
    return render(request, "webdes.html", {"webdes": webdes})
