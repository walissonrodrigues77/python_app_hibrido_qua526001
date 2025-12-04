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
