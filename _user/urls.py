'''
Created on 2013-07-23

@author: Ian
'''
from django.conf.urls import patterns, url

from _user import views

urlpatterns = patterns('',
                       url(r'^$', views.userDashboard, name='userDashboard'),
                       url(r'^comment/$', views.userComment, name='userComment'),
                       url(r'^labbook/tag/(?P<subject_url>[^/]+)/$', views.userLabbook, name='userLabbookTag'),
                       url(r'^labbook/$', views.userLabbook, name='userLabbook'),
                       url(r'^labbook/user/(?P<user_url>[^/]+)/$', views.userLabbookNameTag, name='userLabbookName'),
                       url(r'^labbook/user/(?P<user_url>[^/]+)/tag/(?P<subject_url>[^/]+)/$', views.userLabbookNameTag, name='userLabbookNameTag'),
                       url(r'^labbook/submit/textform/(?P<subject_url>[^/]+)/$', views.userLabbookTextForm, name='userLabbookTextForm'),
                       url(r'^labbook/submit/imageform/(?P<subject_url>[^/]+)/$', views.userLabbookImageForm, name='userLabbookImageForm'),
                       url(r'^labbook/submit/timelikeform/(?P<subject_url>[^/]+)/$', views.userLabbookTimelikeForm, name='userLabbookTimelikeForm'),
                       url(r'^labbook/submit/dataform/(?P<subject_url>[^/]+)/$', views.userLabbookDataForm, name='userLabbookDataForm'),
                       url(r'^labbook/submit/textform/$', views.userLabbookTextForm, name='userLabbookTextForm'),
                       url(r'^labbook/submit/imageform/$', views.userLabbookImageForm, name='userLabbookImageForm'),
                       url(r'^labbook/submit/timelikeform/$', views.userLabbookTimelikeForm, name='userLabbookTimelikeForm'),
                       url(r'^labbook/submit/dataform/$', views.userLabbookDataForm, name='userLabbookDataForm'),
                       url(r'^search/labbook/$', views.userSearchForm, name='userSearchForm'),
                       url(r'^publish/$', views.userPublish, name='userPublish'),
                       url(r'^publish/manage/$', views.userPublish, name='userPublishManage'),
                       url(r'^labbook/submit/updateform/$', views.userLabbookUpdateForm, name='userLabbookUpdateForm'),
                      )
