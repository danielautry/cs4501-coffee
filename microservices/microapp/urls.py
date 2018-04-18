from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<num>[0-9]+)/',views.viewProduct, name = 'viewProduct'),
    url(r'^product/destroy/(?P<num>[0-9]+)/',views.destroyProduct, name = 'destroyProduct'),
    url(r'^product/create/',views.createProduct, name = 'createProduct'),
    url(r'^customer/(?P<num>[0-9]+)/',views.viewCustomer, name = 'viewCustomer'),
    url(r'^customer/destroy/(?P<num>[0-9]+)/',views.destroyCustomer, name = 'destroyCustomer'),
    url(r'^customer/create/',views.createCustomer, name = 'createCustomer'),
    #url(r'^sale/(?P<num>[0-9]+)/',views.viewSale, name = 'viewSale'),
    #url(r'^sale/destroy/(?P<num>[0-9]+)/',views.destroySale, name = 'destroySale'),
    #url(r'^sale/create/',views.createSale, name = 'createSale'),
    url(r'^customer/login/',views.login, name = 'login'),

    #jeremy tuesday edits below
    # url(r'^review/(?P<num>[0-9]+)/',views.viewReview, name = 'viewReview'),
    # #url(r'^review/destroy/(?P<num>[0-9]+)/',views.destroyReview, name = 'destroyReview'),
    # url(r'^review/create/',views.createReview, name = 'createReview'),

]
