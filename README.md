# Para executar o projeto, inicialmente, crie um ambiente virtual com o comando:
python -m venv venv

# Ative o ambiente virutal usando o comando:
. venv/bin/activate

# Instale o python-flask no seu ambiente virtual
pip install flask

# Rode o seu projeto utilizando o comando
flask run

# Modifique seu arquivo app.py para adicionar uma nova rota

# Salve o arquivo requirements.txt para que seja possível iniciar o ambiente virtual em outros ambientes. Sempre que instalar novos pacotes, atualize o seu arquivo requirements.txt
pip freeze > requirements.txt

# Para iniciar esse ambiente em outros codespaces ou em máquinas locais, você pode iniciar um novo ambiente virtual com a sequência de comandos a seguir:
python -m venv venv  
. venv/bin/activate
pip install -r requirements.txt
