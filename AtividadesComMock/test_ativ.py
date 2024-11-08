import pytest
from unittest.mock import patch, Mock
from ativ import calcular_valor_total, obter_pedido_com_valor_total, BancoDeDados
import requests

# Fixture para o banco de dados
@pytest.fixture
def banco_de_dados_simulado():
    banco = BancoDeDados()
    banco.buscar_pedido = Mock(return_value={"id": 1, "cliente": "João"})
    return banco

# Teste para a função calcular_valor_total()
def test_calcular_valor_total():
    with patch('ativ.requests.get') as mock_get:
        # Simulando a resposta da API
        mock_get.return_value.json.return_value = [
            {"preco": 10.0, "quantidade": 2},
            {"preco": 20.0, "quantidade": 1}
        ]
        
        total = calcular_valor_total(1)
        assert total == 40.0  # 10*2 + 20*1 = 40

# Teste para a função obter_pedido_com_valor_total()
def test_obter_pedido_com_valor_total(banco_de_dados_simulado):
    with patch('ativ.calcular_valor_total', return_value=40.0):
        pedido = obter_pedido_com_valor_total(1, banco_de_dados_simulado)
        assert pedido["valor_total"] == 40.0
        assert pedido["cliente"] == "João"
