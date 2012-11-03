from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', 'show.views.index'),
    url(r'^shows/(\d+)/$', 'shows.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
