from django.conf.urls import patterns, include, url

from test_project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^municipalities/(?P<province_code>.{0,50})/$',
        views.get_municipalities_json, name='get_municipalities_json'),
)
