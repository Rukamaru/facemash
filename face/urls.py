from django.conf.urls import include, url
from face import views

urlpatterns = [
    url(r'^$', views.index, name="base"),
    url(r'^connexion/$', views.connexion, name="connexion"),
    url(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),

    # url(r'^article/(?P<id_article>\d+)$', 'view_article'),
    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles'),
]

