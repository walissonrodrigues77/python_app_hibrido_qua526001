
import flet as ft

def main(page: ft.Page):
    page.title = "App Flet com Botão e Entrada"
    # Adicionar o modo de tema LIGHT (corrigindo o erro que você teve anteriormente)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 1. Variáveis de Controle
    # Campo de entrada de texto
    nome = ft.TextField(label="Digite seu nome", width=250)
    # Campo de texto para exibir a saída
    nome_saida = ft.Text("Seu nome aparecerá aqui.")

    # 2. Função de Clique (Callback)
    def exibir_nome(e):
        # Pega o valor do campo de entrada 'nome'
        texto_digitado = nome.value
        
        # Define o texto de saída
        nome_saida.value = f"Olá, {texto_digitado}!"
        
        # Atualiza a página para mostrar o novo texto
        page.update()

    # 3. Criação e Adição do Layout
    # Usamos ft.Row para alinhar o campo de entrada e o botão lado a lado
    layout_principal = ft.Row(
        [
            # Primeiro item: O campo de entrada
            nome,
            
            # Segundo item: O Botão
            ft.ElevatedButton("Enviar", on_click=exibir_nome),
        ],
        alignment=ft.MainAxisAlignment.CENTER # Centraliza o grupo na linha
    )

    # 4. Adicionar os controles à página
    page.add(
        layout_principal,  # O campo de entrada e o botão (em linha)
        nome_saida         # O campo de saída (abaixo)
    )

# Execução do Aplicativo Flet
if __name__ == "__main__":
    ft.app(target=main)