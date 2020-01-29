from django.shortcuts import render
from webdes.models import Webdes

# Create your views here

def do_search(request):
    webdes = Webdes.objects.filter(name__icontains=request.GET['q'])
    return render(request, "webdes.html", {"webdes": webdes})
