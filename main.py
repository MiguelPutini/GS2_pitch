import os
import sys
import webbrowser
import threading
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI

# Carrega variáveis de ambiente do .env
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Chave OPENAI_API_KEY não configurada no arquivo .env!")

client = OpenAI(api_key=API_KEY)

app = Flask(__name__, static_folder=".")
CORS(app)

PORT = int(os.getenv("PORT", 5000))

SYSTEM_PROMPT = """Você é o Citizen Assist AI, um assistente digital inteligente criado para orientar cidadãos brasileiros sobre serviços públicos, documentos, direitos e orientações comunitárias, no contexto da Global Solution 2026.2 da FIAP (Ciência da Computação).

DIRETRIZES FUNDAMENTAIS:
1. Responda sempre em português brasileiro claro, acessível e direto ao ponto.
2. Sempre que cabível, cite portais e fontes oficiais (ex: gov.br, Receita Federal, INSS, Poupatempo, Detran, Procon).
3. NUNCA se apresente como um órgão oficial do governo. Deixe claro que você é um assistente de orientação e triagem.
4. Conscientização de Privacidade e LGPD: Se o usuário enviar dados sensíveis (como senhas, dados de cartão ou números sigilosos), alerte-o para não compartilhar dados privados na internet.
5. Incorpore orientações de energia sustentável quando oportuno (ex: Tarifa Social de Energia, dicas de eficiência, cálculo de custo-benefício de energia solar).
6. Estruture a resposta com passos numerados ou tópicos para facilitar a leitura.
7. Ao final de respostas sobre emissão de documentos ou serviços, acrescente uma indicação oficial:
   "📌 Fonte de validação oficial: portal gov.br"
"""

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True)
        if not data or "messages" not in data or not isinstance(data["messages"], list):
            return jsonify({"error": "Formato de requisição inválido. Envie uma lista de mensagens."}), 400

        user_messages = data["messages"][-8:]  # Mantém até 8 mensagens no contexto

        messages_payload = [{"role": "system", "content": SYSTEM_PROMPT}]
        for m in user_messages:
            if isinstance(m, dict) and "role" in m and "content" in m:
                messages_payload.append({
                    "role": m["role"],
                    "content": str(m["content"])
                })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_payload,
            max_tokens=900,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"[ERRO NO CHAT]: {e}", file=sys.stderr)
        return jsonify({"error": f"Erro interno ao processar a consulta: {str(e)}"}), 500

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    print("=" * 60)
    print("   CITIZEN ASSIST AI - GLOBAL SOLUTION 2026.2 (FIAP)")
    print("   Tema: CitizenTech - Tecnologia para a Vida Cotidiana")
    print("=" * 60)
    print(f" Servidor iniciado em: http://localhost:{PORT}")
    print(" Abrindo seu navegador...")
    print(" Pressione Ctrl+C para encerrar o servidor.")
    print("=" * 60)

    # Abre o navegador em thread separada após 1 segundo
    threading.Timer(1.2, open_browser).start()

    app.run(host="0.0.0.0", port=PORT, debug=False)
