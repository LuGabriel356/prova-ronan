from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():

    
    
    nome = str(request.form['nome'])
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    
    imc = peso / (altura * altura)

    return render_template('index.html',
                           nome = nome,
                           peso = peso,
                           altura = altura,
                           imc = imc)

@app.route('/equipe')
def equipe():

    return render_template('equipe.html')














if __name__ == '__main__':
    app.run(debug=True)