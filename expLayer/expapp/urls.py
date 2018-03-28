from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coffeeProduct/(?P<num>[0-9]+)/',views.viewCoffeeProduct, name = 'viewCoffeeProduct'),
    
]
