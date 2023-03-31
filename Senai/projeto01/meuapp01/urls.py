from django.urls import path
from . import views

urlpatterns = [
    path('', views.raiz, name="raizapp"),
    path('cadastro', views.cadastro, name="cadastroapp"),
    path('login', views.login, name="loginapp")
]
