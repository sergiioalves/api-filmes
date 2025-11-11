from flask import Flask, jsonify

app = Flask(__name__)

filmes = [
    {"id": 1, "titulo": "O Poderoso Chefão", "ano": 1972},
    {"id": 2, "titulo": "Interestelar", "ano": 2014},
    {"id": 3, "titulo": "Clube da Luta", "ano": 1999}
]


@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(filmes)


@app.route('/filmes/<int:id>', methods=['GET'])
def buscar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            return jsonify(filme)
    return jsonify({"erro": "Filme não encontrado"}), 404


@app.route('/filmes/<int:id>', methods=['DELETE'])
def deletar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            filmes.remove(filme)
            return jsonify({"mensagem": "Filme removido com sucesso"})
    return jsonify({"erro": "Filme não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
