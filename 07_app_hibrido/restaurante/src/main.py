
import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Downloader Simples"
    page.padding = 20

    url_input = ft.TextField(label="URL do arquivo", width=400)
    status = ft.Text("")

    def baixar_arquivo(e):
        url = url_input.value.strip()
        if not url:
            status.value = "❗ Digite uma URL."
            page.update()
            return

        try:
            status.value = "⏳ Baixando..."
            page.update()

            r = requests.get(url, stream=True)
            nome_arquivo = url.split("/")[-1]

            with open(nome_arquivo, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            status.value = f"✔ Download concluído: {nome_arquivo}"
        except Exception as err:
            status.value = "❌ Erro ao baixar."
            print(err)

        page.update()

    page.add(
        url_input,
        ft.ElevatedButton("Baixar", on_click=baixar_arquivo),
        status
    )

ft.app(target=main)