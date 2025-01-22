import os
import requests
import json
import pandas
import sqlite3

'''
endpoints= {
    "summoner_profile_icon": "https://ddragon.leagueoflegends.com/cdn/15.1.1/img/profileicon/{id}.png",
    "champion_icon": "https://ddragon.leagueoflegends.com/cdn/15.1.1/img/champion/{championName}.png",
    "champion_splash_art": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{championName}_{skinId}.jpg",
    "spell_icon": "https://ddragon.leagueoflegends.com/cdn/15.1.1/img/spell/{spellName}.png",
    "item_icon": "https://ddragon.leagueoflegends.com/cdn/15.1.1/img/item/{itemId}.png",
    "summoner_spell_icon": "https://ddragon.leagueoflegends.com/cdn/15.1.1/img/spell/{summonerSpell}.png",
    "champion_list": "https://ddragon.leagueoflegends.com/cdn/15.1.1/data/en_US/champion.json",
    "item_list": "https://ddragon.leagueoflegends.com/cdn/15.1.1/data/en_US/item.json",
    "versions": "https://ddragon.leagueoflegends.com/api/versions.json"}
'''

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
    if response.status_code == 200:
        playerInfo = requests.get(f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{req["puuid"]}?api_key={get_api_key()}")
        playerInfo =playerInfo.json()
        print(playerInfo)
        return playerInfo

    return None


__all__ = ['get_summoner']