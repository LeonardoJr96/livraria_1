from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListRetrieveSerializer, LivroSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .favorito import FavoritoSerializer, FavoritoRetriveSerializer
from .presente import PresenteSerializer
from .compra import (
    CompraListSerializer, # novo
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)

from .livro import (
    LivroAjustarEstoqueSerializer, # novo
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)