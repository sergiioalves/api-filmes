from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {"id": 1, "titulo": "Matrix", "ano": 1999},
    {"id": 2, "titulo": "Interestelar", "ano": 2014}
]

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(filmes), 200

@app.route('/filmes/<int:filme_id>', methods=['DELETE'])
def deletar_filme(filme_id):
    filme = next((f for f in filmes if f["id"] == filme_id), None)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404
    filmes.remove(filme)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
