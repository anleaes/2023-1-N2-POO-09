from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'generos'

router = routers.DefaultRouter()
router.register('generos', views.CategoryViewSet, basename='generos')

urlpatterns = [
    path('', include(router.urls) )
]