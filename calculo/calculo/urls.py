from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^calculus/', include('calculus.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
