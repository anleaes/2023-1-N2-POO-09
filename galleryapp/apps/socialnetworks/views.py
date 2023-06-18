from django.shortcuts import render

# Create your views here.
from .models import Socialnetwork
from rest_framework import viewsets
from .serializer import SocialnetworkSerializer

# Após o comentario "# Create your views here." e crie as views "Socialnetwork".

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer  