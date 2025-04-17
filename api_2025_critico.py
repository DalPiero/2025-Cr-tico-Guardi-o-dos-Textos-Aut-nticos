from flask import Flask, jsonify, request
from pathlib import Path

app = Flask(__name__)
FILE_PATH = Path("2025_Critico_Instrucoes.md")

@app.route('/api/instrucoes', methods=['GET'])
def get_instrucoes():
    if not FILE_PATH.exists():
        return jsonify({"error": "Arquivo não encontrado"}), 404
    content = FILE_PATH.read_text(encoding="utf-8")
    return jsonify({"conteudo": content})

@app.route('/api/instrucoes', methods=['POST'])
def save_instrucoes():
    data = request.json
    conteudo = data.get("conteudo")
    if not conteudo or not isinstance(conteudo, str):
        return jsonify({"error": "Conteúdo inválido"}), 400
    FILE_PATH.write_text(conteudo, encoding="utf-8")
    return jsonify({"message": "Instruções salvas com sucesso"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)