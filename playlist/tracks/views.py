from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers import TrackSerializer, ProducerSerializer, LabelSerializer
from .models import Track, Producer, Label
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions, generics


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    #authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,]


class TrackView(generics.RetrieveAPIView):
    serializer_class = TrackSerializer
    #authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        items = Track.objects.all()
        return Response({'items': items})


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
