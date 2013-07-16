'''
Created on 2013-07-14

@author: Ian
'''
from django.conf.urls import patterns, url

from _home import views

urlpatterns = patterns('',
                       url(r'^(?P<subject_url>.*)/$', views.getSubject, name='subject'),
                       url(r'^$', views.home, name='index'),
                      )
