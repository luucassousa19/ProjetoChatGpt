from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Configurar as credenciais da API do OpenAI
openai_api_key = "sk-pnaZ688dlyvw4R7DcKmqT3BlbkFJ0tXWtZyTuRBmgChJaXI"
url = 'https://api.openai.com/v1/chat/completions'
headers = {'Authorization': f'Bearer {openai_api_key}'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = enviar_pergunta(pergunta)
        return render_template('index.html', pergunta=pergunta, resposta=resposta)
    else:
        return render_template('index.html')

def enviar_pergunta(pergunta):
    mensagem_inicial = 'Voce a partir de agora é um agente do imais...'
    dados_dataframe = 'Seus dados do DataFrame aqui...'

    historico_dialogo = [
        {'role': 'system', 'content': mensagem_inicial},
        {'role': 'user', 'content': dados_dataframe},
        {'role': 'user', 'content': pergunta}
    ]

    response = requests.post(url, json={'messages': historico_dialogo, 'model': 'gpt-3.5-turbo'}, headers=headers)
    if response.status_code == 200:
        result = response.json()
        resposta = result['choices'][0]['message']['content']
        return resposta
    else:
        return 'Erro ao chamar a API'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
