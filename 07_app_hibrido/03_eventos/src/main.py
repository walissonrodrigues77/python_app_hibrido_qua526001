import flet as ft


def main(page: ft.Page):

    # função do evento
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()

        # Propriedades da página
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive" 
    page.theme_mode = ft.ThemeMode.LIGHT

    # Declaração d variáveis
    nome = ft.TextField(label="Informe seu Nome: ", on_submit=exibir_nome)
    nome_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=35, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        
        nome,
        ft.ElevatedButton("Enviar", on_click=exibir_nome),
        nome_saida
     )



ft.app(main)



