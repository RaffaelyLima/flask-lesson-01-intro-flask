from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem vindos a disciplina de Desenvolvimento Web'

@app.route('/email')
@app.route('/contato')
def contato():
    return 'alba.lopes@ifrn.edu.br'

@app.route('/endereco')
def endereco():
    return 'Rua Brusque, 2629'