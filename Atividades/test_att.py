import pytest
import math
from att import *

def test_email_valido():
    assert email_valido("email@valido.com")
    assert not email_valido("email_invalido")

def test_eh_par():
    assert eh_par(2)
    assert not eh_par(3)

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1

def test_quadrado():
    assert quadrado(4) == 16

def test_eh_positivo():
    assert eh_positivo(10)
    assert not eh_positivo(-5)

def test_verificar_maioridade():
    assert verificar_maioridade(18) == 'maior de idade'
    assert verificar_maioridade(17) == 'menor de idade'

def test_classificar_temperatura():
    assert classificar_temperatura(-5) == 'frio'
    assert classificar_temperatura(10) == 'moderado'
    assert classificar_temperatura(30) == 'quente'

def test_avaliar_nota():
    assert avaliar_nota(8) == 'aprovado'
    assert avaliar_nota(6) == 'recuperacao'
    assert avaliar_nota(3) == 'reprovado'

def test_pode_votar():
    assert pode_votar(20) == 'voto obrigatório'
    assert pode_votar(17) == 'voto facultativo'
    assert pode_votar(15) == 'não pode votar'

def test_avaliar_produto():
    assert avaliar_produto(5) == 'excelente'
    assert avaliar_produto(4) == 'bom'
    assert avaliar_produto(3) == 'regular'
    assert avaliar_produto(2) == 'ruim'
    assert avaliar_produto(1) == 'péssimo'
    assert avaliar_produto(0) == 'valor inválido'

def test_soma():
    assert soma(1, 2) == 3

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_multiplica():
    assert multiplica(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Erro: divisão por zero não permitida."

def test_area_circulo():
    assert area_circulo(3) == math.pi * 9
    assert area_circulo(-3) == "Erro: o raio não pode ser negativo."

def test_area_retangulo():
    assert area_retangulo(4, 5) == 20
    assert area_retangulo(-4, 5) == "Erro: largura e altura devem ser não-negativos."
