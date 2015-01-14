from django.conf.urls import patterns, include, url
from django.contrib import admin
from movielib import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'), 
    url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movie_delete'),

    
)
