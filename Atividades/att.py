import math

# Função de verificação de email
def email_valido(email):
    return '@' in email and '.' in email

# Função para verificar se um número é par  
def eh_par(n):
    return n % 2 == 0

# Função para calcular o fatorial 
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# Função para calcular o quadrado
def quadrado(n):
    return n ** 2

# Função para verificar se é positivo
def eh_positivo(n):
    return n > 0

# Função para verificar a maioridade
def verificar_maioridade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

# Função para classificar temperatura
def classificar_temperatura(temp):
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'

# Função para avaliar nota
def avaliar_nota(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'

# Função para verificar se pode votar
def pode_votar(idade):
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'

# Função para avaliar produto
def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'

# Função para soma
def soma(a, b):
    return a + b

# Função para subtração
def subtrai(a, b):
    return a - b

# Função para multiplicação
def multiplica(a, b):
    return a * b

# Função para divisão
def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero não permitida."
    return a / b

# Função para calcular a área de um círculo
def area_circulo(raio):
    if raio < 0:
        return "Erro: o raio não pode ser negativo."
    return math.pi * (raio ** 2)

# Função para calcular a área de um retângulo
def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Erro: largura e altura devem ser não-negativos."
    return largura * altura
