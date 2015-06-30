#-*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'comparateur/accueil.html', {'date': datetime.now()})
