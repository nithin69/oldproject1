from django.conf.urls import patterns, url, include

from ams import views
from views import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView


urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
		url(r'^about/$', views.about, name='about'),
                url(r'^scolarship/$', views.scolarship, name='scolarship'),
                url(r'^jobs/$', views.jobs, name='jobs'),       
                url(r'^events/$', views.events, name='events'),
                url(r'^news/$', views.news, name='news'),       
                url(r'^activites/$', views.activites, name='activites'),
		url(r'^contact/$', views.contact, name='contact'),
		url(r'^founder/$', views.founder, name='founder'),
                url(r'^secretery/$', views.secretery, name='secretery'),       
		url(r'^faq/$', views.faq, name='faq'),
		url(r'^video/$', views.video, name='video'),
##                url(r'^resource/$', views.resources, name='resource'),
                url(r'^image/$', views.image, name='image'),
                url(r'^audio/$', views.audio, name='audio'),
		url(r'^hallbooking/$', views.hallbooking, name='hallbooking'),
		url(r'^members/$', views.members, name='members'),                       
		url(r'^roombooking/$', views.roombooking, name='roombooking'),
		url(r'^searchbook/$', views.searchbook, name='searchbook'),
                url(r'^websites/$', views.websites, name='websites'),
                url(r'^search/$', views.search, name='search'),
		url(r'^sms/$', views.sms, name='sms'),
                url(r'^search2/$', views.search2, name='search2'),
         




)
