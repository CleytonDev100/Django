from django.urls import path
from . import views

urlpatterns = [
    path("", views.raiz, name="raiz"),
    path("produto/", views.produtos, name="produto")
]
