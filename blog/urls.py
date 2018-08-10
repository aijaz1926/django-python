from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_blog, name="get_all_blog"),
    url(r'^(?P<slug>[-\w]+)/$', views.get_blog, name="get_blog"),
]