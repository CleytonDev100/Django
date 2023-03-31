# Generated by Django 4.1.6 on 2023-03-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp01', '0007_preco_produto_delete_produtos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabela',
            old_name='nome_produto',
            new_name='cod_produto',
        ),
        migrations.AlterField(
            model_name='preco_produto',
            name='data_preco',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='preco_produto',
            name='preco_produto',
            field=models.FloatField(),
        ),
    ]
