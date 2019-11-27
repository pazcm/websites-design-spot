from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GetInTouchForm

# Create your views here

def contact(request):
    if request.method == 'GET':
        form = GetInTouchForm()
    else:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')
