import summoner
import os
import flet as ft
import getApi as api

 
def main(page: ft.Page):
    def search(e):
        if nick.value:
            if tag.value =="":
                tagline= "br1"
            else:
                tagline= tag.value 
                tagline= tagline.replace("#","")
            page.add(ft.Text(str(api.get_summoner("AMERICAS",nick.value, tagline)),size=30, color="blue"))
            nick.value = ""
            tag.value=""
            page.update()
        

    nick = ft.TextField(label="Nome de Invocador",hint_text="Nickname", max_length=18)
    tag = ft.TextField(label="Tagline",prefix_text="#",hint_text="BR1", max_length=5)
    page.add(nick,tag, ft.IconButton(icon=ft.Icons.SEARCH, on_click=search))
    page.add()
    #page.add(ft.Text(str(user), size=30, color="blue"))


ft.app(main)