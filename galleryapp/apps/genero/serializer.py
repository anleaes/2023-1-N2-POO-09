from .models import Genero
from rest_framework import serializers

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
