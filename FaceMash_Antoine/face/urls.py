from django.conf.urls import url
from face import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addition/(?P<number_1>[0-9]+)/(?P<number_2>[0-9]+)/$', views.addition, name="addition"),
    url(r'^(?P<question_id>[0-9]+)/details/$', views.details, name="details"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name="votes"),
]