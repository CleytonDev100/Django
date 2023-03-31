from django.contrib import admin
from .models import Usuario, Tabela, Preco_produto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tabela)
admin.site.register(Preco_produto)
