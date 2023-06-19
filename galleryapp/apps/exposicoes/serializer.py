from .models import Exposicao
from rest_framework import serializers

class ExposicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposicao
        fields = '__all__'