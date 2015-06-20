from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'comparateur.views.home', name='home'),
)