from rest_framework import serializers
from meuapp import models

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = "__all__"
