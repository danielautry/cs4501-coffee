from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<num>[0-9]+)/',views.viewProduct, name = 'viewProduct'),
    url(r'^customer/create/',views.createCustomer, name = 'createCustomer'),
    url(r'^customer/(?P<num>[0-9]+)/',views.viewCustomer, name = 'viewCustomer'),
    url(r'^customer/login/',views.login, name = 'login'),
    url(r'^customer/logout/',views.logout, name = 'logout'),
    url(r'^product/create/',views.createProduct, name = 'createProduct'),
    url(r'^search/',views.search, name = 'search'),
    url(r'^viewAllProducts/', views.viewAllProducts, name = 'viewAllProducts')
]
