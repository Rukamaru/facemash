from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationFormWithInactiveUsersOkay

def index(request):
    return render(request, "base.html", {
        'latest_question_list': Question.objects.order_by('-pub_date')[:5],
    })


def connexion(request):
    # if request.method == 'POST':
    form = AuthenticationFormWithInactiveUsersOkay(request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "base.html", {
                    'success_message':"Bienvenue " + username + " !"
                })
            else:
                return render(request, "face/connexion.html", {
                    'error_message':"Vous n'etes pas un utilisateur actif."
                })
        else:
            return render(request, "face/connexion.html", {
                'error_message':"L'identifiant ou le mot de passe est incorrect."
            })
    # else:
    #    form = AuthenticationFormWithInactiveUsersOkay()

    return render(request, "face/connexion.html",)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question_id)

    return render(request, 'face/detail.html', {
        'context': 'detail',
        'question': question,
        'choices': choices,

    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question_id)
    votes = Choice.objects.filter(question=question_id).values("votes")

    numberVote = 0
    for vote in votes:
        numberVote += vote["votes"]

    return render(request, 'face/results.html', {
        'question': question,
        'choices': choices,
        'votes': numberVote,
    })

@login_required
def vote(request, question_id):
    """if not request.user.is_authenticated():
        return render(request, 'face/detail.html', {
            'error_message': "Veuillez vous connecter avant de voter.",
        })"""

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = get_object_or_404(Choice, pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "face/detail.html", {
            'question': question,
            'error_message': "Une erreur s'est produite. Veuillez reessayer.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('face:results', args=(question.id,)))
