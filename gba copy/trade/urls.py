from django.conf.urls import patterns, url
from trade import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^New', views.new, name='new'),
                       url(r'^Insert', views.insert, name='insert'),
)