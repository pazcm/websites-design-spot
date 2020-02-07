# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import GetInTouchForm

def contactView(request):
    if request.method == 'GET':
        form = GetInTouchForm()
    else:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact_name = form.cleaned_data['contact_name']
            try:
                send_mail(message, from_email, contact_name, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, "success.html")