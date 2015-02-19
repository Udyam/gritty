from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from gritty import views

#first argument is empty because views don't have common prefix
urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name="home"),
    url(r'^login$',views.login,name='login'),
    url(r'^register$',views.login,name='register')
)
