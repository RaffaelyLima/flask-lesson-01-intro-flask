# Primeiro projeto em Python Flask

## Crie um novo codespace

Ao abrir esse repositório, inicialmente você deve criar um novo Codespace. Para tanto, clique no botão verde "Code", em seguida, clique no botão "Create codespace on main", ilustrado na figura a seguir (ou clicando no símbolo +). Você verá que abrirá uma janela com o ambiente de programação do Visual Studio Code.
<img width="621" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/817f9226-e836-4911-9b29-289f65611c76">

P.S: Caso esteja familiarizado com o Visual Studio Code ou deseje utilizá-lo em sua máquina local, sinta-se a vontade para  clonar o repositório localmente e efetivar os comandos a partir da sua máquina.

## Inicie um ambiente virtual

No codespace criado, inicie um novo ambiente virtual. A criação do ambiente virtual é importante para possiblitar isolar a instalação dos novos pacotes que serão necessários e facilitar a replicação desse ambiente de codificação em outras máquinas ou em outros codespaces. Para tanto execute o comando abaixo na guia do terminal no Visual Studio Code:

`python -m venv venv`

Na sequência, ative o ambiente virtual criado usando o comando
`
. venv/bin/activate
`

## Instale o python-flask no seu ambiente virtual
Para que sua aplicação possa utilizar o Python-Flask é necessário instalar o pacote associado a esse framework. Para tanto, digite no terminal o comando:
`
pip install flask
`

## Execute o seu projeto
Para executar projetos Flask, você deve digitar no terminal o comando:

`
flask run
`

## Abra o seu projeto no navegador
Siga o link gerado após a execução do *flask run* para ver o resultado da sua aplicação.

# Modificando seu projeto Flask

## Altere o arquivo app.py
No seu arquivo app.py, adicione uma nova rota. Salve o projeto e efetue 

## Salvando as configurações do seu codespace
Para que seja possível iniciar esse ambiente virtual em outros codespaces ou na sua máquina local, é importante que você salve as informações dos pacotes que foram instalados por meio do pip install no arquivo requirements.txt. Para isso, execute o seguinte comando no terminal:

`
pip freeze > requirements.txt

`
## Atualize o repositório com as modificações realizadas
Até o momento, as modificações que foram realizadas não foram refletidas no seu repositório de código. Para que seja possível salvar as modificações, você deve fazer commit dessas alterações. Isso pode ser feito por meio da linha de comando ou por meio da interface gráfica do Visual Studio Code.
Para fazer pela interface gráfica, pode

# Para iniciar esse ambiente em outros codespaces ou em máquinas locais, você pode iniciar um novo ambiente virtual com a sequência de comandos a seguir:
python -m venv venv  
. venv/bin/activate
pip install -r requirements.txt
