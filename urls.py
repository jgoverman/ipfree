""" urlconf for IPFREE app """

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()
from ipfree import views

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # url(r'^$', 'sclouds3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.search, name='search'),
    url(r'^ipfree/', views.search, name='search'),
    url(r'^ipadd/', views.addip, name='addip'),
    #url(r'', include('base.urls')),
)

