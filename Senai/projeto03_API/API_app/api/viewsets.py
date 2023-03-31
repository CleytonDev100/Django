from rest_framework import viewsets
from API_app.api import serializers
from API_app import models

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
