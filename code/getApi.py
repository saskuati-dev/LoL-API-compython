import os
import requests
import json
import pandas
import sqlite3

def get_api_key():
    try:
        api_key = os.getenv("API_KEY", "chave-padrao") 
        if not api_key:
            raise ValueError('A chave da API não foi encontrada\nDefina a sua chave no arquivo .env, no formato: \nAPI_KEY="{sua chave}"\nSe não tiver o arquivo, crie.')
        return api_key
        
    except Exception as e:
        print(f"Erro ao carregar a chave API: {e}")
        return None
    

def get_summoner( server :str, nick :str, tagline :str):
    url = f"https://{server}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nick}/{tagline}?api_key={get_api_key()}"
    response = requests.get(url)
    req = response.json()
    print(f"{nick}\n{tagline}\n{server}\n\n{req}\n{url}")
    return req



__all__ = ['get_summoner']