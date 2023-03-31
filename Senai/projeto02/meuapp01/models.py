from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=60, null=False)
    email = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=False)
    tipo_user = models.CharField(max_length=4, null=True)

    def __str__(self) -> str:
        return self.cpf


class Tabela(models.Model):
    nome_produto = models.CharField(max_length=60, null=False)
    nome_descricao = models.CharField(max_length=60, null=False)

    def __str__(self) -> str:
        return self.nome_produto


class Preco_produto(models.Model):
    preco_produto = models.FloatField()
    data_preco = models.DateTimeField(auto_now=True)
    nome_produto = models.ForeignKey(Tabela, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cod_produto
