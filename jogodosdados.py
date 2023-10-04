import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/jogar_dados')
def jogar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    resultado = ""

    if soma == 7 or soma == 11:
        resultado = "Você ganhou!"
    elif soma == 2 or soma == 3 or soma == 12:
        resultado = "Você perdeu!"
    else:
        resultado = "Você continua jogando. Tente obter a mesma soma novamente ou 7 para ganhar."

    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run()
