from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testGet/',views.testGet, name = 'testGet'),
    url(r'^testPost/',views.testPost, name = 'testPost')
]
