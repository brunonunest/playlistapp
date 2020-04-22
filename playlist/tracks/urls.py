from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'producers', views.ProducerViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'labels', views.LabelViewSet)

urlpatterns = [
    path('playlist/', views.TrackView.as_view()),
    path('', include(router.urls)),
]