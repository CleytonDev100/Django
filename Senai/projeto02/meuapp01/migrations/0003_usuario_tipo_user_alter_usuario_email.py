# Generated by Django 4.1.6 on 2023-02-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp01', '0002_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_user',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]