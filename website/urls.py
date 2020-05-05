"""Defines urls for website"""


from django.conf.urls import url
from . import views 

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^listings$', views.listings, name='listings'),
    url(r'^myListings$', views.myListings, name='myListings'),
    url(r'^create$', views.create, name='create'),
    url(r'^filter/(?P<tag>\w+)$', views.filter, name='filter'),
]


