import flet as ft
from pytubefix import YouTube
import os
import threading

def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.horizontal_alignment = "center"

    # Criar pastas
    os.makedirs("videos", exist_ok=True)
    os.makedirs("audios", exist_ok=True)

    # LOGO PEQUENA
    logo = ft.Image(
        src="images.jpg",  # coloque sua mini logo aqui
        width=84,
        height=84,
        fit=ft.ImageFit.CONTAIN
    )

    # Campo de URL com valor inicial simulando placeholder
    url = ft.TextField(
        value="Cole a URL aqui...",
        width=450,
        bgcolor="#FFFFFF",
        border_radius=12,
        border_color="#9B30FF",
        focused_border_color="#8B008B",
    )

    def clear_on_focus(e):
        if url.value == "Cole a URL aqui...":
            url.value = ""
            page.update()

    url.on_focus = clear_on_focus

    # Informações do vídeo
    video_thumb = ft.Image(
        src=None,
        width=150,
        height=90,
        fit=ft.ImageFit.COVER,
        border_radius=10,
        visible=False
    )
    titulo = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#3E4756")
    canal = ft.Text("", size=14, color="#3E4756")
    duracao = ft.Text("", size=14, color="#3E4756")
    views = ft.Text("", size=14, color="#3E4756")

    video_info = ft.Column([video_thumb, titulo, canal, duracao, views], spacing=8, visible=False)

    # Barra de progresso e status
    progress = ft.ProgressBar(visible=False, width=450, color="#9B30FF", bgcolor="#E0CFFF")
    status = ft.Text("", size=14, text_align="center", color="#3E4756")

    # Funções de status
    def set_status(msg, color):
        status.value = msg
        status.color = color
        page.update()

    def update_video_info(yt):
        mins = yt.length // 60
        secs = yt.length % 60
        titulo.value = yt.title
        canal.value = f"Canal: {yt.author}"
        duracao.value = f"Duração: {mins}:{secs:02d}"
        views.value = f"Visualizações: {yt.views:,}"
        video_thumb.src = yt.thumbnail_url
        video_info.visible = True
        video_thumb.visible = True
        page.update()

    # Função de download de vídeo
    def baixar_video(e):
        if not url.value.strip() or url.value == "Cole a URL aqui...":
            return set_status("Insira uma URL válida", "#A63D40")

        def task():
            try:
                progress.visible = True
                set_status("Carregando metadados...", "#3E4756")
                yt = YouTube(url.value.strip())
                update_video_info(yt)
                set_status("Baixando vídeo...", "#3E4756")
                stream = yt.streams.get_highest_resolution()
                if not stream:
                    return set_status("Não foi possível baixar.", "#A63D40")
                stream.download("videos")
                progress.visible = False
                set_status("Vídeo baixado com sucesso!", "#2A7F62")
            except Exception as e:
                progress.visible = False
                set_status(f"Erro: {e}", "#A63D40")

        threading.Thread(target=task, daemon=True).start()

    # Função de download de áudio
    def baixar_audio(e):
        if not url.value.strip() or url.value == "Cole a URL aqui...":
            return set_status("Insira uma URL válida", "#A63D40")

        def task():
            try:
                progress.visible = True
                set_status("Carregando metadados...", "#3E4756")
                yt = YouTube(url.value.strip())
                update_video_info(yt)
                set_status("Baixando áudio...", "#3E4756")
                stream = yt.streams.filter(only_audio=True).first()
                if not stream:
                    return set_status("Não foi possível baixar.", "#A63D40")
                audio = stream.download("audios")
                base, _ = os.path.splitext(audio)
                os.rename(audio, base + ".mp3")
                progress.visible = False
                set_status("Áudio salvo como MP3!", "#2A7F62")
            except Exception as e:
                progress.visible = False
                set_status(f"Erro: {e}", "#A63D40")

        threading.Thread(target=task, daemon=True).start()

    # Função limpar campos
    def limpar(e):
        url.value = "Cole a URL aqui..."
        video_info.visible = False
        video_thumb.visible = False
        status.value = ""
        progress.visible = False
        page.update()

    # Botões com cores vivas
    btn_video = ft.ElevatedButton(
        "Baixar Vídeo",
        icon="download",
        bgcolor="#9B30FF",  # roxo choque
        color="white",
        width=200,
        on_click=baixar_video,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    btn_audio = ft.ElevatedButton(
        "Baixar Áudio",
        icon="audiotrack",
        bgcolor="#8B008B",  # rosa escuro
        color="white",
        width=200,
        on_click=baixar_audio,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    btn_clear = ft.IconButton(icon="close", on_click=limpar, icon_color="#3E4756")

    # Card central
    card = ft.Container(
        content=ft.Column(
            [
                ft.Row([logo, ft.Text("YouTube Downloader", size=26, weight=ft.FontWeight.BOLD, color="#FFFFFF")], spacing=10, vertical_alignment="center"),
                ft.Row([url, btn_clear], alignment="center"),
                video_info,
                ft.Row([btn_video, btn_audio], alignment="center"),
                progress,
                status
            ],
            spacing=15
        ),
        width=520,
        padding=25,
        bgcolor="#FFFFFF",
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=20, color="#B4C2D3", spread_radius=1)
    )

    # Fundo degradê com cores vivas e preenchimento das áreas "vazias"
    background = ft.Container(
        content=card,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#9B30FF", "#DA70D6", "#8B008B"]  # roxo choque -> lilás -> rosa escuro
        ),
        padding=50,
        alignment=ft.alignment.center
    )

    page.add(background)

ft.app(main)

