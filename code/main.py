import summoner
import os
import flet as ft
import getApi as api

 
def main(page: ft.Page):
    
    page.window_maximized = True


    def search(e):
        if nick.value:
            if tag.value =="":
                tagline= "BR1"
            else:
                tagline= tag.value 
                tagline= tagline.replace("#","")
            #page.add(ft.Text(str(api.get_summoner("AMERICAS",nick.value, tagline)),size=30, color="blue"))
            invocador =api.get_summoner("AMERICAS",nick.value, tagline)
            if invocador==None:
                return
            
            img = ft.Image(src=f"https://ddragon.leagueoflegends.com/cdn/15.1.1/img/profileicon/{invocador['profileIconId']}.png", expand = True,fit="cover"  )
            icone = ft.Container(
            img,
            width=100,
            height=100,
            border_radius= 25,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
                )
            dados_base =[]
            
            
            dados_base.append(
                            ft.Container(
                                content=ft.Text(f"{nick.value} #{tagline}" ),
                                alignment=ft.alignment.center,
                                height= 40,
                                width=200,
                                bgcolor="#282a36",
                                border_radius=ft.border_radius.all(25),
                                shadow=ft.BoxShadow(
                                    spread_radius=2,
                                    blur_radius=0,
                                    color=ft.Colors.BLUE_GREY_300,
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                )
                            )
                        )
            
            dados_base.append(
                            ft.Container(
                                content=ft.Text(f"Nivel: {invocador['summonerLevel']}" ),
                                alignment=ft.alignment.center,
                                height= 40,
                                width=150,
                                bgcolor="#282a36",
                                border_radius=ft.border_radius.all(25),
                                shadow=ft.BoxShadow(
                                    spread_radius=2,
                                    blur_radius=0,
                                    color=ft.Colors.BLUE_GREY_300,
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                )
                            )
                        )

            page.add(
                ft.Row(controls=[icone, ft.Column(controls=dados_base, alignment="left", expand= True)],alignment="center")

            )
            nick.value = ""
            tag.value=""
            page.update()

    nick = ft.TextField(label="Nome de Invocador",hint_text="Nickname", max_length=18, on_submit=search,expand=True)
    tag = ft.TextField(label="Tagline",prefix_text="#",hint_text="BR1", max_length=4,on_submit=search,expand=True)
    buscar = ft.IconButton(icon=ft.Icons.SEARCH, on_click=search)
    page.add(
        ft.Row(controls=[nick, tag, buscar], alignment="center")
    )
    #page.add(ft.Text(str(user), size=30, color="blue"))


ft.app(main)