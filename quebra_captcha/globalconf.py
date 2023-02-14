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

caminho_captcha = getenv('caminho_captcha')

region = getenv('region')
key = getenv('key')


