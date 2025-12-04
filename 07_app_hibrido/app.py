import flet as ft
from pytubefix import YouTube
import os, threading

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
        src="images.jpg",  # mini logo
        width=60,
        height=60,
        fit=ft.ImageFit.CONTAIN
    )

    # Campo de URL
    url = ft.TextField(
        label="Cole a URL do vídeo",
        width=450,
        bgcolor="#FFFFFF",
        border_radius=12,
        border_color="#8A2BE2",  # roxo vibrante
        focused_border_color="#7B68EE",  # lilás
    )

    # Informações do vídeo
    video_thumb = ft.Image(
        src=None,
        width=160,
        height=90,
        fit=ft.ImageFit.COVER,
        border_radius=10,
        visible=False
    )
    titulo = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#1C1C1C")
    canal = ft.Text("", size=14, color="#1C1C1C")
    duracao = ft.Text("", size=14, color="#1C1C1C")
    views = ft.Text("", size=14, color="#1C1C1C")

    video_info = ft.Column([video_thumb, titulo, canal, duracao, views], spacing=6, visible=False)

    # Barra de progresso e status
    progress = ft.ProgressBar(visible=False, width=450, color="#8A2BE2", bgcolor="#E6E6FA")
    status = ft.Text("", size=14, text_align="center", color="#1C1C1C")

    # Funções auxiliares
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

    # Download de vídeo
    def baixar_video(e):
        if not url.value.strip():
            return set_status("Insira uma URL válida", "#A63D40")
        def task():
            try:
                progress.visible = True
                set_status("Carregando metadados...", "#1C1C1C")
                yt = YouTube(url.value.strip())
                update_video_info(yt)
                set_status("Baixando vídeo...", "#1C1C1C")
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

    # Download de áudio
    def baixar_audio(e):
        if not url.value.strip():
            return set_status("Insira uma URL válida", "#A63D40")
        def task():
            try:
                progress.visible = True
                set_status("Carregando metadados...", "#1C1C1C")
                yt = YouTube(url.value.strip())
                update_video_info(yt)
                set_status("Baixando áudio...", "#1C1C1C")
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

    # Limpar campos
    def limpar(e):
        url.value = ""
        video_info.visible = False
        video_thumb.visible = False
        status.value = ""
        progress.visible = False
        page.update()

    # Botões
    btn_video = ft.ElevatedButton(
        "Baixar Vídeo",
        icon="download",
        bgcolor="#8A2BE2",
        color="white",
        width=200,
        on_click=baixar_video,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )
    btn_audio = ft.ElevatedButton(
        "Baixar Áudio",
        icon="audiotrack",
        bgcolor="#7B68EE",
        color="white",
        width=200,
        on_click=baixar_audio,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )
    btn_clear = ft.IconButton(icon="close", on_click=limpar, icon_color="#1C1C1C")

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

    # Fundo degradê com cores vivas e harmônicas
    background = ft.Container(
        content=card,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#8A2BE2", "#DA70D6", "#7B68EE"]  # roxo -> lilás -> violeta
        ),
        padding=50,
        alignment=ft.alignment.center
    )

    page.add(background)

ft.app(main)



# app lista de tarefas 
import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas (Versão Antiga Completa)"
    page.window_width = 400
    page.window_height = 600

    entrada = ft.TextField(label="Nova tarefa", expand=True)
    lista = ft.Column()

    # === Remover tarefa ===
    def remover_tarefa(container):
        lista.controls.remove(container)
        page.update()

    # === Adicionar tarefa ===
    def adicionar_tarefa(e):
        texto = entrada.value.strip()
        if texto == "":
            return

        # Checkbox da tarefa
        checkbox = ft.Checkbox(label=texto, expand=True)

        # Campo de edição (só aparece quando clicamos em editar)
        campo_edicao = ft.TextField(value=texto, expand=True, visible=False)

        # === Alternar edição ===
        def editar_tarefa(e):
            checkbox.visible = False
            campo_edicao.visible = True
            botao_editar.visible = False
            botao_salvar.visible = True
            page.update()

        # === Salvar texto editado ===
        def salvar_edicao(e):
            novo_texto = campo_edicao.value.strip()
            if novo_texto:
                checkbox.label = novo_texto
            checkbox.visible = True
            campo_edicao.visible = False
            botao_editar.visible = True
            botao_salvar.visible = False
            page.update()

        # Botões
        botao_editar = ft.ElevatedButton(
            "Editar",
            width=70,
            on_click=editar_tarefa
        )

        botao_salvar = ft.ElevatedButton(
            "Salvar",
            width=70,
            on_click=salvar_edicao,
            visible=False
        )

        botao_remover = ft.ElevatedButton(
            "Remover",
            width=80,
            bgcolor="red",
            color="white",
            on_click=lambda e: remover_tarefa(container),
        )

        # Container da tarefa
        container = ft.Column(
            [
                ft.Row([checkbox, campo_edicao]),
                ft.Row([botao_editar, botao_salvar, botao_remover],
                       alignment="spaceBetween")
            ]
        )

        lista.controls.append(container)
        entrada.value = ""
        page.update()

    # Layout principal
    page.add(
        ft.Row([
            entrada,
            ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa),
        ]),
        ft.Container(height=10),
        lista
    )

ft.app(target=main)


#jogo de paciencia

import flet as ft
import random

# -------- FUNÇÕES BÁSICAS --------
def gerar_baralho():
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cartas = [v + n for n in naipes for v in valores]
    random.shuffle(cartas)
    return cartas


def cor_carta(c):
    if c.endswith("♥") or c.endswith("♦"):
        return "red"
    return "white"


def main(page: ft.Page):
    page.title = "Paciência Interativo (Compatível Antigo)"
    page.bgcolor = "#1F1F1F"

    # Baralho
    baralho = gerar_baralho()

    # 4 colunas iniciais com 5 cartas cada (viradas)
    colunas = []
    for _ in range(4):
        col = [{"valor": baralho.pop(), "virada": False} for _ in range(5)]
        colunas.append(col)

    # Guarda carta selecionada
    selecionada = {"col": None, "index": None}

    # Interface de colunas
    col_views = [ft.Column(spacing=3) for _ in range(4)]
    msg = ft.Text("", size=22, color="yellow")

    # -------- ATUALIZA A TELA --------
    def atualizar():
        for i in range(4):
            col_views[i].controls.clear()

            if len(colunas[i]) == 0:
                col_views[i].controls.append(
                    ft.Container(
                        content=ft.Text("(vazio)", color="white"),
                        bgcolor="#333333",
                        padding=8,
                        border_radius=6,
                        width=100,
                        alignment=ft.alignment.center
                    )
                )
                continue

            # Renderizar cartas
            for idx, carta in enumerate(colunas[i]):

                # Mostrar valor ou virada
                if carta["virada"]:
                    txt = carta["valor"]
                    cor = cor_carta(carta["valor"])
                else:
                    txt = "▒▒▒"
                    cor = "white"

                # Se for a carta selecionada → destacar
                is_sel = (selecionada["col"] == i and selecionada["index"] == idx)

                # Botão-carta
                def make_press(i=i, idx=idx):
                    return lambda e: click_carta(i, idx)

                col_views[i].controls.append(
                    ft.ElevatedButton(
                        txt,
                        on_click=make_press(),
                        bgcolor="#444444" if carta["virada"] else "#555555",
                        color=cor,
                        width=100,
                        style=ft.ButtonStyle(
                            side=ft.BorderSide(3, "#00FFAA") if is_sel else ft.BorderSide(1, "white"),
                            shape=ft.RoundedRectangleBorder(radius=6)
                        )
                    )
                )

        # Vitória
        if all(len(c) == 0 for c in colunas):
            msg.value = "🎉 Você ganhou!"
        else:
            msg.value = ""

        page.update()

    # -------- LÓGICA DE CLIQUE --------
    def click_carta(col, idx):
        carta = colunas[col][idx]

        # Se a carta estiver virada → virar
        if not carta["virada"]:
            carta["virada"] = True
            atualizar()
            return

        # Se nada estiver selecionado → selecionar carta
        if selecionada["col"] is None:
            selecionada["col"] = col
            selecionada["index"] = idx
            atualizar()
            return

        # Se clicar na mesma carta → desselecionar
        if selecionada["col"] == col and selecionada["index"] == idx:
            selecionada["col"] = None
            selecionada["index"] = None
            atualizar()
            return

        # Tentar mover a carta selecionada para a coluna clicada
        mover_carta(selecionada["col"], selecionada["index"], col)

        # Resetar seleção
        selecionada["col"] = None
        selecionada["index"] = None

        atualizar()

    # -------- MOVER CARTA --------
    def mover_carta(origem, idx, dest):
        if origem == dest:
            return

        # Pega a carta
        carta = colunas[origem][idx]

        # Remove da origem
        del colunas[origem][idx]

        # Insere no destino
        colunas[dest].append(carta)

    # -------- BOTÃO DE COMPRA --------
    carta_comprada = ft.Text("Nenhuma carta comprada", color="white")

    def comprar(e):
        if len(baralho) == 0:
            carta_comprada.value = "Baralho vazio!"
        else:
            nova = {"valor": baralho.pop(), "virada": True}
            colunas[0].append(nova)
            carta_comprada.value = f"Carta comprada: {nova['valor']}"

        atualizar()

    comprar_btn = ft.ElevatedButton(
        "Comprar carta",
        on_click=comprar,
        bgcolor="#00D46A",
        color="black"
    )

    # -------- LAYOUT --------
    page.add(
        ft.Text("PACIÊNCIA INTERATIVO", size=26, weight="bold", color="#00FFD5"),
        ft.Container(height=10),

        ft.Row([
            ft.Container(col_views[0], expand=True),
            ft.Container(col_views[1], expand=True)
        ]),
        ft.Row([
            ft.Container(col_views[2], expand=True),
            ft.Container(col_views[3], expand=True)
        ]),

        ft.Container(height=20),
        comprar_btn,
        carta_comprada,

        ft.Container(height=20),
        msg
    )


if __name__ == "__main__":
    ft.app(target=main)
