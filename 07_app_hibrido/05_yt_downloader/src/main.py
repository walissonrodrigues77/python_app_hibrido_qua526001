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
    os.makedirs(caminho_audios, exist_ok=True)

    # componentes da interface gráfica
    titulo = ft.Text("Use uma URL", color=ft.Colors.BLACK, size=20, weight=ft.FontWeight.BOLD)
    url = ft.TextField(
        label="Cole a URL do vídeo do YouTube aqui",
        width=400,
        border_radius=10
    )

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")
    logo_cabecalho = ft.Image(src=logo_path, width=300, height=200)

    # componente para mostrar informações do vídeo
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400
    )

    # barra de progresso
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    # texto de status
    status_text = ft.Text(
        "",
        color=ft.Colors.BLACK,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # mostra as informações de vídeo na interface
    def mostrar_info_videos(yt):
        try:
            # limpa o container
            video_info.content.controls.clear()

            # adiciona informações do vídeo
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título: {yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duração: {yt.length/60}:{yt.length%60:02d}", size=12),
                    ft.Text(f"Visualizações: {yt.views:,}", size=12),
                ]
            )

            video_info.visible = True
            page.update()

        except Exception as e:
            status_text.value = f"Erro ao obter informações: {str(e)}."
            status_text.color = ft.Colors.RED
            page.update()
    
    # função para baixar vídeo
    def baixar_video(e):
        if not url.value.strip():
            status_text.value = "Por favor, insira uma URL válida."
            status_text.color = ft.Colors.ORANGE
            page.update()
            # REVIEW: verificar se return é necessário nessa parte do código
        
        def donwload_thread():
            try:
                # mostra progresso
                progress_bar.visible = True
                status_text.value = "Analisando vídeo..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cria objeto do youtube
                yt = YouTube(url.value.strip())

                # mostra as informações do vídeo
                mostrar_info_videos(yt)

                # inicia download
                status_text.value = f"Baixando vídeo: {yt.title}..."
                page.update()

                # pega a maior resolução possível
                stream = yt.streams.get_highest_resolution()

                # TODO: fazer if else do stream
                if stream:
                    stream.download(caminho_videos)

                    # sucesso
                    progress_bar.visible = False
                    status_text.value = "Download concluído com sucesso."
                    status_text.color = ft.Colors.GREEN
                    page.update()
                else:
                    progress_bar.visible = False
                    status_text.value = "Não foi possível baixar o vídeo."
                    status_text.color = ft.Colors.RED
                    page.update()

            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro {str(e)}."
                status_text.color = ft.Colors.RED
                page.update()
        
        # executa em thread separada para não travar a interface
        threading.Thread(target=donwload_thread, daemon=True).start()
    
    # extrair o audio do vídeo
    def extrair_audio(e):
        if not url.value.strip():
            status_text.value = "Favor inserir uma URL"
            status_text.color = ft.Colors.ORANGE
            page.update()
        
        def download_thread():
            try:
                progress_bar.visible = True
                status_text.value = "Analisando vídeo..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cira objeto YouTube
                yt = YouTube(url.value.strip())

                # mostra informações do vídeo
                mostrar_info_videos(yt)

                # inicia download do áudio
                status_text.value = f"Extraindo audio de {yt.title}..."
                page.update()

                stream = yt.streams.filter(only_audio=True).first()
                if stream:
                    audio_file = stream.download(caminho_audios)

                    # renomeia para mp3
                    base, extens = os.path.splitext(audio_file)
                    novo_audio = base + ".mp3"
                    os.rename(audio_file, novo_audio)

                    # sucesso
                    progress_bar.visible = False
                    status_text.value = f"Audio salvo como {os.path.basename(novo_audio)}"
                    status_text.color = ft.Colors.GREEN
                    page.update()
                else:
                    progress_bar.visible = False
                    status_text.value = "Não foi possível baixar o áudio."
                    status_text.color = ft.Colors.RED
                    page.update()

            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro: {str(e)}."
                status_text.color = ft.Colors.RED
                page.update()
        
        # executa em thread separada para não travar a interface
        threading.Thread(target=download_thread, daemon=True).start()
    
    # limpa campos e reinicia a interface
    def limpar_campos(e):
        url.value = ""
        video_info.visible = False
        progress_bar.visible = False
        status_text.value = ""
        page.update()
    
    # interface
    video_btn = ft.ElevatedButton(
        text="Baixar vídeo",
        width=150,
        on_click=baixar_video,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            elevation=3,
            text_style=ft.TextStyle(size=18)
        )
    )
    audio_btn = ft.ElevatedButton(
        text="Baixar audio",
        width=150,
        on_click=extrair_audio,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN,
            color=ft.Colors.WHITE,
            elevation=3,
            text_style=ft.TextStyle(size=18)
        )
    )
    clear_btn = ft.IconButton(
        on_click=limpar_campos,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY,
            color=ft.Colors.WHITE,
            elevation=1
        )
    )
    linha_url = ft.Row(
        [url, clear_btn],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    botoes = ft.Row(
        [video_btn, audio_btn],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
        
    page.add(
       ft.Column(
            [
                logo_cabecalho, linha_url,
                ft.Divider(height=0, color=ft.Colors.TRANSPARENT),
                video_info, botoes,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                progress_bar, status_text
                
            ],
            spacing=15,
            alignment=ft.CrossAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
            
        )
    )

ft.app(main)