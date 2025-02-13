from core.serializers import ProdutoRetrieveSerializer, ProdutoSerializer, ProdutoListSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Produto


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoRetrieveSerializer
        return ProdutoSerializer
