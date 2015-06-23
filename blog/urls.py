__author__ = 'michel'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/new/', views.post_new),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]


