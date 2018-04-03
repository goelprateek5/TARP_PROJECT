from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
urlpatterns=[
    url(r'^$', views.index, name='index'),

    #url(r'^results$', views.save_req, name='save_req'),
    url(r'^confirmbook$', views.confirm, name='confirm'),

    
    url(r'^service-worker.js', (TemplateView.as_view(
    template_name="service-worker.js",
    content_type='application/javascript',
)), name='service-worker.js'),
    
    
]