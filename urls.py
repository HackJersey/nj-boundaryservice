from django.conf.urls.defaults import include, patterns, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
#import django.views.generic.base.TemplateView 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.example.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'', include('boundaryservice.urls')),
    (r'', include('finder.urls')),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /1.0/", mimetype="text/plain"))
#    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', 'mimetype': 'text/plain'}),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
