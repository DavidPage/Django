from django.conf.urls import patterns, url
from team import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^new', views.new, name='new'),
                       url(r'^insert', views.insert, name='insert'),
)