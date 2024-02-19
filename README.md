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

Veja a figura a seguir como deve ser a execução desse comando:
<img width="761" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/f48c6886-59b2-4cbe-9b94-e793f9ee401f">

Após a execução desse comando, observe que no seu projeto foi criada uma nova pasta chamada **venv**. Essa pasta representa o seu ambiente virtual. 
Não se preocupe, pois esses novos arquivos não serão adicionados ao seu repositório, pois a pasta venv foi previamente adicionada ao arquivo .gitignore. Esse arquivo é um arquivo bastante importante em repositórios, pois informam quais pastas e arquivos não devem ter mudanças rastreadas. Pode abrir o arquivo .gitignore e verificar o seu conteúdo. 

Na sequência, ative o ambiente virtual criado usando o comando a seguir no terminal:
```
. venv/bin/activate
```

O comando acima é bastante importante e ele deve ser executado sempre que você for retomar a codificação em um ambiente virtual já criado. Observe que ao executar esse comando, o terminal passou a exibir o prefixo (venv) antes do início da linha de comando:
<img width="610" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/186e9eca-efa5-426b-9019-6afbc673a129">

Assim, da próxima vez que abrir seu codespace, não esqueça de digitar esse comando.

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

<img width="788" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/ab967623-e7ae-469c-8c41-095404fc7670">

Observe a exibição da mensagem de retorno do método index no seu navegador.
Para parar a execução da aplicação, basta pressionar as teclas CTRL + C, conforme sugerido no terminal.

# Modificando seu projeto Flask

## Altere o arquivo app.py
O arquivo app.py possui os direcionamentos necessários para a criação de um projeto Python Flask. Observe o conteúdo desse arquivo. 
Em projetos web, rotas são usadas nas aplicações atuais para possibilitar associar funções a URLs (Uniform  Resource Locator) e deixar o acesso às funções mais elegantes.

No exemplo anterior, o **@app.route('/')** foi usado para associar a função **index** à URL base da aplicação. Assim, quando o usuário digitar no navegador o endereço da aplicação (por exemplo: https://super-dollop-v5rv95prx9xfxg64-5000.app.github.dev/), será apresentado na tela o retorno da função index.

Valide o conceito de rotas criando uma nova função no arquivo app.py e associando essa função a uma nova rota (a rota /contato):

```
@app.route('/')
def index():
  return 'Essa é minha primeira aplicação em Flask!'

@app.route('/contato')
def contato():
  return 'alba.lopes@ifrn.edu.br'
```

Caso seu projeto ainda esteja executando, pressione CTRL + C no terminal e na sequência, execute novamente o comando 

```
flask run
```

Siga o link para abrir o seu projeto no navegador e após o endereço da aplicação, digite `/contato` como no exemplo a seguir:

<img width="448" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/fb63fd0c-fd8d-4cac-a9bb-f894ccea499e">


## Salvando as configurações do seu codespace
Para que seja possível iniciar esse ambiente virtual em outros codespaces ou na sua máquina local, é importante que você salve as informações dos pacotes que foram instalados por meio do pip install no arquivo requirements.txt. Para isso, execute o seguinte comando no terminal:

```
pip freeze > requirements.txt
```

## Atualize o repositório com as modificações realizadas
Até o momento, as modificações que foram realizadas não foram refletidas no seu repositório de código. Para que seja possível salvar as modificações, você deve fazer commit dessas alterações. Isso pode ser feito por meio da linha de comando, caso já esteja familiarizado com os comandos git, ou por meio da interface gráfica do Visual Studio Code.
Para fazer pela interface gráfica, na guia lateral, clique no símbolo de versionamento de código.

<img width="426" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/d277c4a7-2e78-4a1d-b725-319819b8dd13">

Na sequência, digite a mensagem que representa as alterações que você fez:

<img width="426" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/84001204-2c14-472d-b7ae-0acb5d1dae22">

Em seguida, clique no botão Commit:

<img width="426" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/2be72449-f63e-4163-95ed-25948c70b295">

Caso apareça uma mensagem perguntando se deseja dar "stage" nas suas modificações, clique em Yes (ou Sim):

<img width="426" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/2f9ee9f7-3260-4e1a-9323-6f6d1cf05195">

Por fim, clique em Sync Changes, para efetivar as modificações no repositório:

<img width="520" alt="image" src="https://github.com/IFRN-ZN-Alba-Lopes/flask-lesson-01-intro-flask/assets/13405201/ef58ec82-6891-42ed-8bfa-fdda6ec6ae14">

## Iniciando novos codespaces com base no repositório salvo
Para iniciar esse ambiente em outros codespaces ou em máquinas locais, você pode iniciar um novo ambiente virtual digitando com a sequência de comandos a seguir no terminal do novo codespace:
```
python -m venv venv
```
```  
. venv/bin/activate
```
```
pip install -r requirements.txt
```
