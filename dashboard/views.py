from django.shortcuts import render, redirect
from main import models
def index(request):
    return render(request, 'dashboard/index.html')

def contactList(request):
    contacts = models.Contact.objects.all().order_by('is_show')
    return render(request, 'dashboard/contact/list.html', {'contacts': contacts})

def updateStatus(request, id):
    contact = models.Contact.objects.get(id=id)
    contact.is_show = True
    contact.save()
    return redirect('contactList')