from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

# Criar pasta de usuários se não existir
if not os.path.exists("Usuarios"):
    os.makedirs("Usuarios")

@app.route('/')
def home():
    return "Backend ativo - Esperando cadastro..."

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    if not nome or not email or not senha:
        return "Dados incompletos!", 400

    # Criar arquivo do usuário
    agora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"Usuarios/{nome}_{agora}.txt"

    with open(filename, 'w') as f:
        f.write(f"Nome: {nome}\n")
        f.write(f"E-mail: {email}\n")
        f.write(f"Senha: {senha}\n")

    print(f"[NOVO CADASTRO] {nome} - {email}")
    return "Cadastro concluído!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))