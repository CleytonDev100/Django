from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests

# Create your views here.


def raiz(requests):
    f = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    f.json()
    cotacao = f["USDBRL"]["code"]
    return render(requests, "home.html", {"cotacao": cotacao})


def cadastro(requests):
    return render(requests, "cadastro.html")


def login(requests):
    return render(requests, "login.html")

