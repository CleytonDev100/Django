from rest_framework import viewsets
from meuapp.api import serializers
from meuapp import models

class Viewset(viewsets.ModelViewSet):
    serializer_class = serializers.Serializer
    queryset = models.Cliente.objects.all()
