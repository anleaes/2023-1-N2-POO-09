from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ingresso'

router = routers.DefaultRouter()
router.register('ingressos', views.IngressosViewSet, basename='ingressos')

urlpatterns = [
    path('', include(router.urls) )
]