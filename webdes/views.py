from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Webdes
from django.views.generic import DetailView

# all webdes view
def all_webdes(request):
    """Return all webdes in the DB and display webdes page"""

    webdes = Webdes.objects.all()
    paginator = Paginator(webdes, 8)  # show 8 webdes each page

    page = request.GET.get('page')
    try:
        webdes = paginator.page(page)
    except PageNotAnInteger:
        # retrieve first page
        webdes = paginator.page(1)
    except EmptyPage:
        # retrieve last page
        webdes = paginator.page(paginator.num_pages)

    return render(request, 'webdes.html', {'webdes': webdes})

# category view
def filter_webdes(request, requestedCategory):
    webdes = Webdes.objects.filter(category=requestedCategory)
    paginator = Paginator(webdes, 8)  # show 8 webdes

    page = request.GET.get('page')
    try:
        webdes = paginator.page(page)
    except PageNotAnInteger:
         # retrieve first page
        webdes = paginator.page(1)
    except EmptyPage:
         # retrieve last page
        webdes = paginator.page(paginator.num_pages)
    return render(request, 'webdes.html', {'webdes': webdes})

# home page view
def webdes_home(request):
    """Return header and all webdes in the DB and display home page"""

    webdes = Webdes.objects.all()
    return render(request, 'index.html', {'webdes': webdes})


# Information about a specific webdes

class WebdesDetail (DetailView):
    model = Webdes
