from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    url(r'^$', views.index, name='index'),
    
]