from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gba.views.home', name='home'),
    # url(r'^gba/', include('gba.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^Team/', include('team.urls', namespace="team")),
    url(r'^Trade/', include('trade.urls', namespace="trade")),
    url(r'^Market/', include('market.urls', namespace="market")),
    url(r'^Competition/', include('competition.urls', namespace="competition")),
    url(r'^Match/', include('match.urls', namespace="match")),
    url(r'^admin/', include(admin.site.urls)),
)
