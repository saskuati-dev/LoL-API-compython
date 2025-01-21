import sqlite3


banco = sqlite3.connect("data_base.db")

cursor = banco.cursor()

try:

    cursor.execute("CREATE TABLE player(nick text, tagline text, puuid text, regiao integer)")
    
        
except Exception as e:
    pass



