from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView


urlpatterns=[
    url(r'^$', views.index, name='index'),    
    url(r'^videos$', views.videos, name='videos'),
    url(r'^music$', views.music, name='music'),
    url(r'^books$', views.books, name='books'),
]