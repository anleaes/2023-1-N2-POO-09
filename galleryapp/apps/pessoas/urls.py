from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pessoa'

router = routers.DefaultRouter()
router.register('pessoas', views.PessoaViewSet, basename='pessoas')

urlpatterns = [
    path('', include(router.urls) )
]