import pytest

# @pytest.fixture
# def listaS():
#     return [1, 2, 3, 4, 5]

# @pytest.fixture
# def nomes():
#     return ["Telin", "Arsenio", "Seco"]

# # def soma(listaS):
# #     return sum(listaS)

# # def multiplicacao(listaS):
# #     resultado = 1
# #     for numero in listaS:
# #         resultado *= numero
# #     return resultado

# # def testSoma(listaS):
# #     assert soma(listaS) == 15

# # def testMultiplicacao(listaS):
# #     assert multiplicacao(listaS) == 120

# # def index(listaS):
# #     return listaS[0], listaS[3]

# # def testIndex(listaS):
# #     assert index(listaS) == (1, 4)

# def dobro(listaS):
#     return sum (x * 2 for x in listaS)

# def testDobro(listaS):
#     assert dobro(listaS) == 30

# def names(nomes):
#     return nomes[0]

# def testNome(nomes):
#     assert names(nomes) == "Telin"

# Definição das funções requisitadas
def acordar_cedo(horario):
    if horario > 6:  # Se acordar após as 6 faça:
        return 'Tente novamente amanhã'
    return 'Você é um guerreiro'

def tempo_exercicio(peso, tempo):
    if tempo > 2:  # Se o tempo de exercicio for maior que 2 faça:
        peso -= 1
        return peso
    pass  # Passa a função sem return

def tem_exercicio(esporte):
    if esporte == 'Descanso':  # Se passar 'Descanso' retorna False
        return False
    return True

# Funções de teste
def testAcordarCedo():
    assert acordar_cedo(5) == 'Você é um guerreiro'
    assert acordar_cedo(7) == 'Tente novamente amanhã'

def testTempoExercicio():
    assert tempo_exercicio(70, 3) == 69
    assert tempo_exercicio(70, 1) == None

def testTemExercicio():
    assert tem_exercicio('Corrida') == True
    assert tem_exercicio('Descanso') == False
