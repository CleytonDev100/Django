from django.shortcuts import render, HttpResponse
from .models import Tabela, Preco_produto


def raiz(requests):
    return render(requests, "raiz.html")


def produtos(request):
    cod = "1"#request.POST.get("ok")
    descricao = "1"#request.POST.get("ok2")
    produto = Tabela(
        nome_produto="1",#cod,
        nome_descricao="1",#descricao,
    )
    produto = Preco_produto(
        preco_produto = "1",#request.POST.get("ok3")
    )
    produto.save()
    return render(request, "informacoes.html")
