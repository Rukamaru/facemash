from django.http import HttpResponse
from django.shortcuts import render

def index(HttpRequest):
    return HttpResponse("Hello world!")

def details(HttpRequest, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(HttpRequest, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def votes(HttpRequest, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def addition(HttpRequest, number_1, number_2):
    total = int(number_1) + int(number_2)
    colors = {'FF0000':'rouge',
            'ED7F10':'orange',
            'FFFF00':'jaune',
            '00FF00':'vert',
            '0000FF':'bleu',
            '4B0082':'indigo',
            '660099':'violet'}

    return render(HttpRequest, "face/index.html", locals())