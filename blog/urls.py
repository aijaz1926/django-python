from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_blog, name="get_all_blog"),
    url(r'^(?P<slug>[-\w]+)/$', views.get_blog, name="get_blog"),
    url(r'^category/(?P<category>[\w]+)/$', views.get_blog_by_category, name="get_blog_by_category"),
    url(r'^(?P<blog_slug>[-\w]+)/comment/$', views.add_comment, name="add_comment"),
]