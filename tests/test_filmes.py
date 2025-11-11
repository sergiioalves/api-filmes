from app import app


def test_listar_filmes():
    cliente = app.test_client()
    resposta = cliente.get('/filmes')
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)


def test_buscar_filme_existente():
    cliente = app.test_client()
    resposta = cliente.get('/filmes/1')
    assert resposta.status_code == 200
    assert resposta.json["titulo"] == "O Poderoso Chefão"


def test_buscar_filme_inexistente():
    cliente = app.test_client()
    resposta = cliente.get('/filmes/999')
    assert resposta.status_code == 404
    assert "erro" in resposta.json


def test_deletar_filme_existente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/2')
    assert resposta.status_code == 200
    assert "mensagem" in resposta.json


def test_deletar_filme_inexistente():
    cliente = app.test_client()
    resposta = cliente.delete('/filmes/999')
    assert resposta.status_code == 404
    assert "erro" in resposta.json
