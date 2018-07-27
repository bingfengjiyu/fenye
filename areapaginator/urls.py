
from django.conf.urls import include, url
from django.contrib import admin
from areapaginator import views



urlpatterns = [
    url(r'^area(?P<pindex>\d*)$',views.area),
    url(r'^session_set$', views.session_set),
    url(r'^session_get$', views.session_get),
]
