from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coffeeProduct/(?P<num>[0-9]+)/', views.showCoffee, name='showCoffee'),
    url(r'^coffee', views.showAllCoffee, name='showAllCoffee'),
]
