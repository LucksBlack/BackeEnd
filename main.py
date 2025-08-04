from flask import Flask, request
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

os.makedirs("Usuarios", exist_ok=True)

@app.route("/", methods=["POST"])
def receber_dados():
    dados = request.get_json()
    nome_arquivo = f"{dados['email'].replace('@', '_').replace('.', '_')}.json"
    caminho = os.path.join("Usuarios", nome_arquivo)
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)
    print(f"[NOVO CADASTRO] {dados}")
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)