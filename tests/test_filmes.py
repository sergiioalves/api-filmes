import json
import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_delete_filme_existente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/1')
    assert resposta.status_code == 204

def test_delete_filme_inexistente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/999')
    assert resposta.status_code == 404
