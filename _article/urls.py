'''
Created on 2013-06-21

@author: Ian
'''
from django.conf.urls import patterns, url

from _article import views

urlpatterns = patterns('',
                       url(r'^(?P<article_url>.*)/$', views.getArticle, name='article'),
                       url(r'^$', views.index, name='index'),
                      )

