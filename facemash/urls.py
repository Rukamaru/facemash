from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('comparateur.urls'), name='home'),
	url(r'^date$', 'date_actuelle'),
)
