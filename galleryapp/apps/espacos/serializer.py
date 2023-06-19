from .models import Espaco
from rest_framework import serializers

class EspacosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espaco
        fields = '__all__'