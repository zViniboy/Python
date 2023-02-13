from dotenv import load_dotenv
from os import getenv

load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

# Acesse as variáveis de ambiente com a função `os.getenv()`
server = getenv('server')
database = getenv('database')
user = getenv('user')
password = getenv('password')

# server = getenv('server')
# database = getenv('database')
# user = getenv('user')
# password = getenv('password')

default_dir = getenv('default_dir')

caminho_pdf = getenv('caminho_pdf')

evidencia_path = getenv('evidencia_path')
# evidencia_path = getenv('evidencia_path')

caminho_captcha = getenv('caminho_captcha')

region = getenv('region')
key = getenv('key')


