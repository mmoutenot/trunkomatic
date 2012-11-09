from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'show.views.index'),
    url(r'^show/(\d+)/$', 'show.views.detail'),
    url(r'^show/add/$', 'show.views.add'),
    url(r'^show/add/performer/&', 'show.views.add_performer'),
    url(r'^admin/', include(admin.site.urls)),
)
