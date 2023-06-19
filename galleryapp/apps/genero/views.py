from django.shortcuts import render

# Create your views here.

from .models import Genero
from rest_framework import viewsets
from .serializer import GeneroSerializer

# Após o comentario "# Create your views here." e crie as views "Genero".

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer  
    
