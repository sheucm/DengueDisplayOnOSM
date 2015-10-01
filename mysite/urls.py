from django.conf.urls import patterns, include, url
from django.contrib import admin
from showpoints.views import show_points
from importDengueData.views import importDengueData

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^points/$', show_points),
    url(r'^importDengueData/$', importDengueData),
    #url(r'^points/', include(showpoints.urls)),
)
