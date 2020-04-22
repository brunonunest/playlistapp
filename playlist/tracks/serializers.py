from .models import Track, Producer, Label
from rest_framework import serializers


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'url', 'name', 'link', 'tracks')


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'url', 'name', 'link', 'producer')


class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producer
        fields = ('id', 'url', 'name', 'link')