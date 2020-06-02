__author__ = 'rt'

from django.conf.urls import patterns, url, include
from ndt import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^about/$', views.about, name='about'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^services/$', views.services, name='services'),
                url(r'^training/$', views.training, name='training'),
                url(r'^careers/$', views.careers, name='careers'),
                url(r'^mission/$', views.mission, name='mission'),       
                     
                       
                       		      
)
