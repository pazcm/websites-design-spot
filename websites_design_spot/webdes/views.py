from django.shortcuts import render
from .models import Webdes

# all webdes view
def all_webdes(request):
    """Return all webdes in the DB and display webdes page"""

    webdes = Webdes.objects.all()
    return render(request, "webdes.html", {"webdes": webdes})

# home page view
def webdes_home(request):
    """Return header and all webdes in the DB and display home page"""

    webdes = Webdes.objects.all()
    return render(request, "index.html", {"webdes": webdes})
