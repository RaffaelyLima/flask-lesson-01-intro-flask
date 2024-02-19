# Primeiro projeto em Python Flask

## Crie um novo codespace

Ao abrir esse repositório, inicialmente você deve criar um novo Codespace. Para tanto, clique no botão verde "Code", em seguida, clique no botão "Create codespace on main", ilustrado na figura a seguir (ou clicando no símbolo +).

<img width="621" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/817f9226-e836-4911-9b29-289f65611c76">

Você verá que abrirá uma janela com o ambiente de programação do Visual Studio Code.

 <img width="949" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/52e79ebd-e63e-4ddd-8392-723221bcb934">

P.S: Caso esteja familiarizado com o Visual Studio Code ou deseje utilizá-lo em sua máquina local, sinta-se a vontade para  clonar o repositório localmente e efetivar os comandos a partir da sua máquina.

## Inicie um ambiente virtual

No codespace criado, inicie um novo ambiente virtual. A criação do ambiente virtual é importante para possiblitar isolar a instalação dos novos pacotes que serão necessários e facilitar a replicação desse ambiente de codificação em outras máquinas ou em outros codespaces. Para tanto execute o comando abaixo na guia do terminal no Visual Studio Code:

```
python -m venv venv
```

<img width="761" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/f48c6886-59b2-4cbe-9b94-e793f9ee401f">

Após a execução desse comando, observe que no seu projeto foi criada uma nova pasta chamada **venv**. Essa pasta representa o seu ambiente virtual. 
Não se preocupe, pois esses novos arquivos não serão adicionados ao seu repositório, pois a pasta venv foi previamente adicionada ao arquivo .gitignore. Esse arquivo é um arquivo bastante importante em repositórios, pois informam quais pastas e arquivos não devem ter mudanças rastreadas. Pode abrir o arquivo .gitignore e verificar o seu conteúdo. 

Na sequência, ative o ambiente virtual criado usando o comando
```
. venv/bin/activate
```

O comando acima é bastante importante e ele deve ser executado sempre que você for retomar a codificação em um ambiente virtual já criado. Observe que ao executar esse comando, o terminal passou a exibir o prefixo (venv) antes do início da linha de comando:
<img width="610" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/186e9eca-efa5-426b-9019-6afbc673a129">


## Instale o python-flask no seu ambiente virtual

Para que sua aplicação possa utilizar o Python-Flask é necessário instalar o pacote associado a esse framework. Para tanto, digite no terminal o comando:
```
pip install flask
```

Observe que, após a execução do comando, foram baixados alguns pacotes essenciais para o funcionamento do framework:

<img width="747" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/ab56b202-7456-4a80-99fb-744c8da42fbe">

## Execute o seu projeto
O projeto compartilhado já possui algumas linhas de código básicas no arquivo app.py. Abra esse arquivo e observe o código a seguir, nas linhas 4 a 6:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo'
```    

Foi programada a rota raiz (/) associada ao método index que exibirá na tela a mensagem 'Olá Mundo'. Para verificar o projeto do que está previamente codificado, você deve digitar no terminal o comando:
```
flask run
```

## Abra o seu projeto no navegador
Siga o link gerado após a execução do *flask run* para ver o resultado da sua aplicação.

# Modificando seu projeto Flask

## Altere o arquivo app.py
No seu arquivo app.py, adicione uma nova rota. Salve o projeto e efetue 

## Salvando as configurações do seu codespace
Para que seja possível iniciar esse ambiente virtual em outros codespaces ou na sua máquina local, é importante que você salve as informações dos pacotes que foram instalados por meio do pip install no arquivo requirements.txt. Para isso, execute o seguinte comando no terminal:

```
pip freeze > requirements.txt
```

## Atualize o repositório com as modificações realizadas
Até o momento, as modificações que foram realizadas não foram refletidas no seu repositório de código. Para que seja possível salvar as modificações, você deve fazer commit dessas alterações. Isso pode ser feito por meio da linha de comando ou por meio da interface gráfica do Visual Studio Code.
Para fazer pela interface gráfica, pode

# Para iniciar esse ambiente em outros codespaces ou em máquinas locais, você pode iniciar um novo ambiente virtual com a sequência de comandos a seguir:
```
python -m venv venv  
. venv/bin/activate
pip install -r requirements.txt
```
