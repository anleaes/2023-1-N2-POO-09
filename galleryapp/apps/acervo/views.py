from django.shortcuts import render

# Create your views here.

from .models import Acervo
from rest_framework import viewsets
from .serializer import AcervoSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Acervo.objects.all()
    serializer_class = AcervoSerializer  
    
