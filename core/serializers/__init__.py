from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListRetrieveSerializer, LivroSerializer
from .livro import (
    LivroAjustarEstoqueSerializer,
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)

from .Produto import ProdutoListRetrieveSerializer, ProdutoSerializer
from .Produto import (
    ProdutoListSerializer,
    ProdutoRetrieveSerializer,
    ProdutoSerializer,
)

from .compra import (
    CompraListSerializer, # novo
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)