from django.conf.urls import url
from . import views
#from django.contrib.auth import auth
#from django.contrib.auth import login
#from django.contrib import auth
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name = 'accounts/login.html',
        redirect_field_name = 'next'
    ), name="login"),


    url(r'^logout/$', auth_views.LogoutView.as_view(
        template_name = 'accounts/logout.html',
        redirect_field_name = next
    ), name="logout"),
]