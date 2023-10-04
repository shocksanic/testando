from flask import Flask, render_template, jsonify, session
from flask_session import Session
import random

app = Flask(__name__)

# Configuração da extensão Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogar_dados')
def jogar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    resultado = ""

    if 'resultado' not in session:
        session['resultado'] = []

    if soma == 7 or soma == 11:
        resultado = "Você ganhou!"
    elif soma == 2 or soma == 3 or soma == 12:
        resultado = "Você perdeu!"
    else:
        resultado = "Você continua jogando. Tente obter a mesma soma novamente ou 7 para ganhar."

    # Passar os valores dos dados para o JavaScript
    return jsonify({"resultado": resultado, "dado1": dado1, "dado2": dado2})

@app.route('/jogar')
def jogar():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
