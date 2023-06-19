from django.shortcuts import render
from .models import Exposicao
from rest_framework import viewsets
from .serializer import ExposicoesSerializer
# Create your views here.
class ExposicoesViewSet(viewsets.ModelViewSet):
    queryset = Exposicao.objects.all()
    serializer_class = ExposicoesSerializer  
