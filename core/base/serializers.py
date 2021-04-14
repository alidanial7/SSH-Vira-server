from rest_framework import serializers

from . import models


class sectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Section
        fields = ['id', 'name']
