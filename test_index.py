import pytest

@pytest.fixture
def listaS():
    return [1, 2, 3, 4, 5]

def soma(listaS):
    return sum(listaS)

def multiplicacao(listaS):
    resultado = 1
    for numero in listaS:
        resultado *= numero
    return resultado

def testSoma(listaS):
    assert soma(listaS) == 15

def testMultiplicacao(listaS):
    assert multiplicacao(listaS) == 120

def index(listaS):
    return listaS[0], listaS[3]

def testIndex(listaS):
    assert index(listaS) == (1, 4)