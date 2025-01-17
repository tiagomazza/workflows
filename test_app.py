# test_app.py

import pytest
from app import sua_funcao  # Importe a função que você deseja testar

def test_sua_funcao():
    resultado = sua_funcao(2, 3)  # Exemplo de chamada da função
    assert resultado == 5          # Verifica se o resultado está correto
