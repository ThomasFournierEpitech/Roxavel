from django.shortcuts import render
from .models import LOLAccountRegistered
from django.contrib.auth.models import User

def home(request):
    context = {
        'accounts': LOLAccountRegistered.objects.filter(owner=request.user)
    }
    return render(request, 'base/home.html', context)

# Create your views here.
