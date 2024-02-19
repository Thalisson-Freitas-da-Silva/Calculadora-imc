# Aplicação feita em Python - Flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    # Receber altura e peso do usuário
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])

    # cálculo imc
    imc = peso / (altura**2)

    # resultado imc
    if imc <= 18.5:
        resultado = "A baixo do peso."
    elif imc >= 18.6 and imc <= 24.9:
        resultado = "Normal"
    elif imc >= 25.0 and imc <= 29.9:
        resultado = "Levemente a cima do peso."
    elif imc >= 30.0 and imc <= 34.9:
        resultado = "Obesidade de grau I"
    elif imc >= 35.0 and imc <= 39.9:
        resultado = "Obesidade de grau II(Severa)"
    else:
        resultado = "Obesidade de grau III(Grave)"
    
    # formatar casas decimais
    imc = '{:.1f}'.format(imc)
    
    # retornar resultados na web
    return render_template('resultado.html', resultado=resultado,imc=imc,peso=peso,altura=altura)
    
if __name__ == '__main__':
    app.run(debug=True)
