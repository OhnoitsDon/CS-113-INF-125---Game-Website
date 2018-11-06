from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^downloads/$', views.downloads, name='downloads')
]
