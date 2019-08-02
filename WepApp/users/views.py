from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from base.forms import GetSummonerForm, GetMultiSummonerForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from cassiopeia import Summoner
from base.models import LOLAccountRegistered
import cassiopeia as lol_api
from django.contrib.auth.models import User
from base.utils import parseListSummonerName


# lol_api.set_riot_api_key('RGAPI-071f6dfd-2d78-4802-98e7-e3bd4017f5de')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfuly!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = GetSummonerForm(request.POST)
        if form.is_valid():
            lol_api.set_default_region('EUW')
            sumname = form.cleaned_data.get('sum_name')
            summoner = Summoner(name=sumname)
            user = request.user
            if summoner.exists:
                alreadyAdd = LOLAccountRegistered.objects.filter(account_id=summoner.puuid, owner=user)
                print (f"summoner.account_id: {summoner.account_id}")
                if not alreadyAdd:
                    newSumInList = LOLAccountRegistered(account_id=summoner.puuid, name=summoner.name, owner=user)
                    newSumInList.save()
                    messages.success(request, f"Summoner name '{summoner.name}' has been added!")
                else:
                    messages.error(request, f"Summoner name '{summoner.name}' is already in your list!")
            else:
                messages.error(request, f"Summoner name '{summoner.name}' doesn't exist.")
            return redirect('profile')
    else:
        form = GetSummonerForm()
    return render(request, 'users/profile.html', {'form': form})

@login_required
def findSummoner(request):
    if request.method == 'POST':
        form = GetMultiSummonerForm(request.POST)
        if form.is_valid():
            lol_api.set_default_region('EUW')
            listSumName = parseListSummonerName(form.cleaned_data.get('sum_name'))
            user = request.user
            context = []
            for sumname in listSumName:
                summoner = Summoner(name=sumname)
                if summoner.exists:
                    alreadyAdd = LOLAccountRegistered.objects.filter(account_id=summoner.puuid, owner=user)
                    print (f"summoner.name: {summoner.name}")
                    if alreadyAdd:
                        context.append(sumname)
            if context:
                for name in context:
                    messages.warning(request, f"Summoner name '{name}' is in your list!")
            else:
                messages.success(request, f"Any of them is in your list!")
            return redirect('findSummoner')
    else:
        form = GetMultiSummonerForm()
    return render(request, 'users/findSummoner.html', {'form': form})

# Create your views here.
