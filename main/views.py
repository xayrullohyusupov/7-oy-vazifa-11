from django.shortcuts import render,redirect
from . import models
from .forms import SignupForm
from django.contrib import auth

def index(request):
    items = models.ChooseItem.objects.all()
    members = models.TeamMember.objects.all()
    partners = models.Partner.objects.all()
    roadmap_items = models.RoadmapItem.objects.all()
    context = {
        'items': items,
        'members': members,
        'partners': partners,
        'roadmap_items': roadmap_items
    }
        
    return render(request, 'front/index.html', context)



def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        models.ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        print(request.POST)
    return render(request, 'front/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('index')