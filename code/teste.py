from dotenv import load_dotenv
import os

load_dotenv('.env')

api_key = os.getenv('API_KEY')
if api_key:
    print(f"Chave da API carregada: {api_key}")
else:
    print("Não foi possível carregar a chave da API.")
