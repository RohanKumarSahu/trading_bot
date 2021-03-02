from rest_framework import viewsets
from . import models
from . import serializers

class DataViewSet(viewsets.ModelViewSet):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer