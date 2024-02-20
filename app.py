from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'PSI é a melhor disciplina!'

@app.route('/contato')
def contato():
    return 'alba.lopes@ifrn.edu.br'

@app.route('/endereco')
def endereco():
    return '<ul><li>Rua Brusque, 2629</li><li>Potengi - Natal/RN</li></ul>'