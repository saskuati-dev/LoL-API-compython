from dotenv import load_dotenv
import os

def get_api_key():
    try:
        load_dotenv('.env')
        api_key  = os.getenv('API_KEY')
        if not api_key:
            raise ValueError('A chave da API não foi encontrada\nDefina a sua chave no arquivo .env, no formato: \nAPI_KEY="{sua chave}"\nSe não tiver o arquivo, crie.')
        return api_key
        
    except Exception as e:
        print(f"Erro ao carregar a chave API: {e}")
        return None