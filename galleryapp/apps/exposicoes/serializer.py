from .models import Exposicao
from rest_framework import serializers

class ExposicoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposicao
        fields = '__all__'