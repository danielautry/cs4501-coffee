from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coffeeProduct/(?P<num>[0-9]+)/', views.showCoffee, name='showCoffee'),
    url(r'^products/', views.detail, name='detail'),
    url(r'^signup/', TemplateView.as_view(template_name='coffeeApp/signup.html')),
    url(r'^account/', views.createAccount, name='createAccount'),
    url(r'^signin/', TemplateView.as_view(template_name='coffeeApp/signin.html')),
    url(r'^login/?next=loggedin', views.login, name='login'),
    url(r'^loggedin/', TemplateView.as_view(template_name='coffeeApp/loggedin.html')),
]
