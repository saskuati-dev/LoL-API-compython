import summoner
import os
import flet as ft
import getApi as api

 
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Text(str(api.get_summoner("AMERICAS",nick.value, tag.value)),size=30, color="blue"))
        nick.value = ""
        tag.value=""
        page.update()

    nick = ft.TextField(hint_text="Nickname")
    tag = ft.TextField(hint_text="Tag")
    page.add(nick,tag, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))
    page.add()
    #page.add(ft.Text(str(user), size=30, color="blue"))


ft.app(main)