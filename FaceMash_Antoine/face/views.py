from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('face/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context))
    return render(request, "face/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def addition(request, nombre_1, nombre_2):
    total = int(nombre_1) + int(nombre_2)
    couleurs = {'FF0000':'rouge',
            'ED7F10':'orange',
            'FFFF00':'jaune',
            '00FF00':'vert',
            '0000FF':'bleu',
            '4B0082':'indigo',
            '660099':'violet'}
    return render(request, 'face/number.html', locals())
