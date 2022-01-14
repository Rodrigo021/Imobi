from django import urls
from django.urls import path
from . import views

#adicionando as urls das funções ao site. Ex: 127.0.0.1/auth/login
urlpatterns = [
    path('cadastro/', views.cadastro, name = "cadastro"),
    path('login/', views.login, name = "login"),
    path('sair/', views.sair, name = "sair")
]