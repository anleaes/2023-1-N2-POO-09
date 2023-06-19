from .models import Acervo
from rest_framework import serializers

class AcervoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acervo
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']