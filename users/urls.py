"""Define URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login Page
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    #Registration Page
    url(r'^register/$', views.register, name='register'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
]

