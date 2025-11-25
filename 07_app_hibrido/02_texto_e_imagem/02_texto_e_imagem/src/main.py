import flet as ft


def main(page: ft.Page):
    

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Minha primeira aplicação", size=90, weight="bold"),
                alignment=ft.alignment.center,
            ),
        ),
        ft.Container(ft.Image(
            src="imagem.jpg",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Não foi possivel carregar a imagem")
        ),
        alignment=ft.alignment.center
    )
 )

ft.app(main)