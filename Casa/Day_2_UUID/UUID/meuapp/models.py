from django.db import models
from uuid import uuid4

# Create your models here.


class Cliente(models.Model):
                                                                                                                                                                                    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=20, null=False)
    telefone = models.CharField(max_length=20, null=False)
