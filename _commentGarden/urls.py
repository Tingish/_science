'''
Created on 2013-08-25

@author: Ian
'''
from django.conf.urls import patterns, url

from _commentGarden import views

urlpatterns = patterns('',
                       url(r'^submit/$', views.submitComment, name='submitComment'),
                       url(r'^$', views.commentIndex, name='comment'),
                      )
