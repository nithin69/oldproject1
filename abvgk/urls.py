__author__ = 'rt'

from django.conf.urls import patterns, url, include
from abvgk import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^schedule/$', views.schedule, name='schedule'),
                url(r'^contact/$', views.contact, name='contact'),
                       		      
)
