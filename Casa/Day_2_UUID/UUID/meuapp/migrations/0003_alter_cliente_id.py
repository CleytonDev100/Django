# Generated by Django 4.1.6 on 2023-03-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0002_alter_cliente_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]