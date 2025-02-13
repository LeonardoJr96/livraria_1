from rest_framework import serializers
from core.models import Presente

class PresenteSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)  # Exibe o nome do usuário em vez do ID

    class Meta:
        model = Presente
        fields = ['id', 'nome', 'descricao', 'usuario']
