#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
	html = """<h1>Bienvenue sur le comparateur de fille du Reseau-GES!</h1>
			<p>Vous pouvez comparer dès maintenant</p>"""
	return HttpResponse(html)
