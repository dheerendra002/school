from django.conf.urls import patterns, include, url
from django.contrib import admin
#import vidyalaya.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('vidyalaya.urls'))
)
