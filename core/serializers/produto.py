from rest_framework.serializers import ModelSerializer

from core.models import Produto

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class ProdutoListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "titulo", "preco")

class ProdutoRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
