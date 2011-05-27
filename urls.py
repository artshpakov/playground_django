from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^switch', 'views.switch_language', name = 'switch_language'),
    url(r'^', include('posts.urls')),
) + staticfiles_urlpatterns()
