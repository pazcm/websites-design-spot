from django.shortcuts import render
from .models import Webdes
from django.views.generic import DetailView

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

# webdes_category view
def webdes_category(request, category):
    """Return the webdes view of a specific category chosen by the user"""

    webdes = Webdes.objects.filter(
        categories__title__contains=category
    ).order_by(
        'webdes_name'
    )
    context = {
        "category": category,
        "webdes": webdes
    }
    return render(request, "webdes_category.html", context)

# Information about a specific webdes

class WebdesDetail (DetailView):
    model = Webdes
