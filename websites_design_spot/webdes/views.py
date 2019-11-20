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

# webdes_category view
"""Return the webdes view of a specific category chosen by the user"""

def webdes_category(request, category):
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