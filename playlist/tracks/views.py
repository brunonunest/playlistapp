from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import TrackSerializer, ProducerSerializer, LabelSerializer
from .models import Track, Producer, Label
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions, generics


"""class HomeView(generics.RetrieveAPIView):
    queryset =
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html' """


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAdminUser]


class TrackView(generics.RetrieveAPIView):
    serializer_class = TrackSerializer, ProducerSerializer, LabelSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tracks.html'

    def get(self, request, *args, **kwargs):
        items = Track.objects.all()
        labels = Label.objects.all()
        producers = Producer.objects.all()
        return Response({'items': items, 'labels': labels, 'producers': producers})


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAdminUser]


class ProducerView(generics.RetrieveAPIView):
    serializer_class = ProducerSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'producers.html'

    def get(self, request, *args, **kwargs):
        items = Producer.objects.all()
        return Response({'items': items})


class LabelViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAdminUser]
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelView(generics.RetrieveAPIView):
    serializer_class = LabelSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'labels.html'

    def get(self, request, *args, **kwargs):
        items = Label.objects.all()
        return Response({'items': items})
