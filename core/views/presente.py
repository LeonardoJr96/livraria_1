from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Presente
from core.serializers import PresenteSerializer

class PresenteViewSet(viewsets.ModelViewSet):
    queryset = Presente.objects.all()
    serializer_class = PresenteSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)  # Associa o presente ao usuário autenticado

    def get_queryset(self):
        return Presente.objects.filter(usuario=self.request.user)  # Retorna apenas os presentes do usuário autenticado
