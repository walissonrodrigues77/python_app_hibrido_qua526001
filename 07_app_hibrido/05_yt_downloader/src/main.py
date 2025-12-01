import flet as ft
from pytubefix import YouTube

import os
import threading


def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"

    # cria as pastas caso não existam

    caminho_videos = 'videos'
    caminho_audios = 'audios'
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios,exist_ok=True)

    # componentes da interface gráfica
    titulo = ft.Text(
        "Use uma URL",
        color=ft.Colors.BLACK,
        size=20,
        weight=ft.FontWeight.BOLD
     )
   
    # compo url
    url = ft.TextField(
        label= "Cole a URL do video do YouTube aqui",
        width= 400,
        border_radius=10,
     )
    
    #logo (opcional)

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")


    #estrutura visual componetes para mostrar informações do video
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50, 
        border_redius=10, 
        width=400 

    )
    # barra de progresso
    progress_bar = ft.progressBar(
        visible= False, 
        width=400,
        color=ft.Colors.BLUE_GREY_100

    )
    # texto de status
    status_text = ft.Text(
        "",
        color=ft.Colors.BLACK, 
        size=14,
        text_align=ft.TextAlign.CENTER

    )
    # mostra as informações de videos na interface
    def mostrar_info_videos(yt):
        try:
            # limpar o container
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título:{yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal:{yt.author}", size=12),
                    ft.Text(f"Duração:{yt.length/60}:{yt.length%60:02d}", size=12),
                    ft.Text(f"Visualizações:{yt.views:,}", size=12),               

                ]

            )

            video_info.visible = True
            page.update()
        
        except Exception as e:
            status_text.value = f"Erro ao obter informações: {str()}."
            status_text.color = ft.Colors.RED
            page.update()

    # função para baixar videos
    def baixar_videos(e):
        if not url.value.strip():
            status_text.value = "Por favor, insira uma URL válida."
            status_text.color = ft.Colors.ORANGE
            page.update()

    def downloader_thread():
        yt=YouTube(url.value.strip())

        #mostra as informações do video
        mostrar_info_videos(yt)

        # inicia downloader
        status_text.value = f"Baixando video: {yt.title}..."
        page.update()

        # pega o maior resolução possivel
        stream = yt.streams.get_highest_resolution()

        # TODO: fazer if else do stream
    except Exception as e:
        progress_bar.visible = False
        status_text.value = f"Erro {str(e)}."
        status-text.value = fy



    page.add(
        ft.SafeArea(
            ft.Container(
            
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
