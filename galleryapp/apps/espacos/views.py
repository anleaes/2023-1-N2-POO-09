from django.shortcuts import render
from .models import Espaco
from rest_framework import viewsets
from .serializer import EspacosSerializer
# Create your views here.
class EspacosViewSet(viewsets.ModelViewSet):
    queryset = Espaco.objects.all()
    serializer_class = EspacosSerializer  