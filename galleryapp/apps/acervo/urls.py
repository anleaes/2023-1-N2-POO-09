
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'acervo'

router = routers.DefaultRouter()
router.register('acervo', views.CategoryViewSet, basename='acervo')

urlpatterns = [
    path('', include(router.urls) )
]