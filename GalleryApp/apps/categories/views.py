from django.shortcuts import render
from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]