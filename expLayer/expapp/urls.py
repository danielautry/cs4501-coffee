from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coffeeProduct/(?P<num>[0-9]+)/',views.viewCoffeeProduct, name = 'viewCoffeeProduct'),
    url(r'^customer/create/',views.createCustomer, name = 'createCustomer'),
    url(r'^customer/(?P<num>[0-9]+)/',views.viewCustomer, name = 'viewCustomer'),
    url(r'^customer/login/',views.login, name = 'login'),

    # Jeremy tuesday edits
    url(r'^review/create/',views.createReview, name = 'createReview')
]
