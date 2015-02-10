from django.conf.urls import patterns, url
# from django.contrib import admin
import webform.views as views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barney.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^order/(.+)/$', views.home, name='active_order'),

)
