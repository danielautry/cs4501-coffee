from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<num>[0-9]+)/', views.showProduct, name='showProduct'),
    url(r'^productList/', views.productList, name='detail'),
    url(r'^signup/', TemplateView.as_view(template_name='marketplace/signup.html')),
    url(r'^account/', views.createAccount, name='createAccount'),
    url(r'^signin/', TemplateView.as_view(template_name='marketplace/signin.html')),
    url(r'^login/?next=loggedin', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^loggedin/', TemplateView.as_view(template_name='marketplace/loggedin.html')),
    url(r'^productForm/', TemplateView.as_view(template_name='marketplace/makeProduct.html'), name='productForm'),
    url(r'^createProduct/', views.createProduct, name='createProduct'),
]
