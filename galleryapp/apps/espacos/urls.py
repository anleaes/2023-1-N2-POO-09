from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'espaco'

router = routers.DefaultRouter()
router.register('espacos', views.EspacosViewSet, basename='espacos')

urlpatterns = [
    path('', include(router.urls) )
]