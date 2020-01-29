from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import GetInTouchForm   

# Create your views here

def contactView(request):
    if request.method == 'GET':
        form = GetInTouchForm()
    else:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_surnam = form.cleaned_data['contact_surname']
            from_email = form.cleaned_data['from_email']
            contact_website = form.cleaned_data['contact_website']
            contact_company = form.cleaned_data['contact_company']
            message = form.cleaned_data['message']
            try:
                send_mail(contact_name, contact_surnam, from_email, contact_website, contact_company, message, ['pazmarta@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
