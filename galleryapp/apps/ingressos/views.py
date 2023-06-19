from django.shortcuts import render
from .models import Ingresso
from rest_framework import viewsets
from .serializer import IngressosSerializer
# Create your views here.
class IngressosViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressosSerializer  