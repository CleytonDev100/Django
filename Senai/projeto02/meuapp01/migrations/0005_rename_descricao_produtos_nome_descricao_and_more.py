# Generated by Django 4.1.6 on 2023-02-24 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp01', '0004_produtos_delete_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='descricao',
            new_name='nome_descricao',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='produto',
            new_name='nome_produto',
        ),
    ]
