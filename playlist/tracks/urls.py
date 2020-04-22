from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'producer', views.ProducerViewSet)
router.register(r'track', views.TrackViewSet)
router.register(r'label', views.LabelViewSet)

urlpatterns = [
    #path('', views.HomeView.as_view()),
    path('labels/', views.LabelView.as_view()),
    path('producers/', views.ProducerView.as_view()),
    path('tracks/', views.TrackView.as_view()),
    path('playlistDRF/', include(router.urls), name='playlistDRF'),
]