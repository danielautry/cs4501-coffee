from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coffeeProduct/(?P<num>[0-9]+)/',views.viewCoffeeProduct, name = 'viewCoffeeProduct'),
    url(r'^coffeeProduct/destroy/(?P<num>[0-9]+)/',views.destroyCoffeeProduct, name = 'destroyCoffeeProduct'),
    url(r'^coffeeProduct/create/',views.createCoffeeProduct, name = 'createCoffeeProduct'),
    url(r'^customer/(?P<num>[0-9]+)/',views.viewCustomer, name = 'viewCustomer'),
    url(r'^customer/destroy/(?P<num>[0-9]+)/',views.destroyCustomer, name = 'destroyCustomer'),
    url(r'^customer/create/',views.createCustomer, name = 'createCustomer'),
    url(r'^sale/(?P<num>[0-9]+)/',views.viewSale, name = 'viewSale'),
    url(r'^sale/destroy/(?P<num>[0-9]+)/',views.destroySale, name = 'destroySale'),
    url(r'^sale/create/',views.createSale, name = 'createSale')

]
