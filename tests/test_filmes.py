import json
from app import app

def test_delete_filme_existente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/1')
    assert resposta.status_code == 204

def test_delete_filme_inexistente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/999')
    assert resposta.status_code == 404
