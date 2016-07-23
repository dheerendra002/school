from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#import vidyalaya.urls
from django.conf.urls import url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^home$', views.index, name='index'),
)

urlpatterns += staticfiles_urlpatterns()

