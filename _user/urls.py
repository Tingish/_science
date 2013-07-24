'''
Created on 2013-07-23

@author: Ian
'''
from django.conf.urls import patterns, url

from _user import views

urlpatterns = patterns('',
                       url(r'^$', views.userDashboard, name='userDashboard'),
                       url(r'^comment/$', views.userComment, name='userComment'),
                       url(r'^labbook/$', views.userLabbook, name='userLabbook'),
                      )
