
from rest_framework import viewsets

from . import serializers
from . import models
# Create your views here.


class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.Section.objects.all().order_by('name')
    serializer_class = serializers.sectionSerializer
