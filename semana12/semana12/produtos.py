from produtos.classes.Produtos import CocaCola, Pepsi
from produtos.classes.Produtos import Dolly, GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml, Tamanho1litro
from produtos.classes.Caracteristicas import Tamanho2litros, Tamanho3litros


def client_code(produto):
    print(produto.operation())


if __name__ == "__main__":
    tamanho = Tamanho600ml()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho600ml()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho2litros()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho3litros()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)
