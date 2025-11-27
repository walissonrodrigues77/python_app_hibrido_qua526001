
# restaurante 

import flet as ft

def main(page: ft.Page):

    page.title = "Orango Tango - Hamburgueria"
    page.theme_mode = "light"
    page.padding = 20
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    # --- Carrinho ---
    carrinho = []

    def atualizar_carrinho():
        total = sum(item["preco"] for item in carrinho)
        carrinho_text.value = f"Carrinho: {len(carrinho)} itens | Total: R$ {total:.2f}"
        page.update()

    def adicionar_item(e):
        produto = e.control.data
        carrinho.append(produto)
        atualizar_carrinho()

    # --- Produtos ---
    hamburgueres = [
        {"nome": "Orango Burger", "preco": 22.90},
        {"nome": "Tango Bacon", "preco": 26.50},
        {"nome": "Macaco Duplo", "preco": 29.90},
    ]

    chickens = [
        {"nome": "Chicken Crispy", "preco": 18.90},
        {"nome": "Monkey Chicken", "preco": 20.50},
        {"nome": "Crispy Duplo", "preco": 24.00},
    ]

    def card_produto(produto):
        return ft.Card(
            content=ft.Container(
                padding=12,
                content=ft.Column([
                    ft.Text(produto["nome"], size=20, weight="bold"),
                    ft.Text(f"R$ {produto['preco']:.2f}", size=16),
                    ft.ElevatedButton(
                        "Adicionar ao Carrinho",
                        data=produto,
                        on_click=adicionar_item,
                        bgcolor="orange",
                        color="white"
                    )
                ])
            )
        )

    lista_hamburgueres = ft.Column(
        controls=[card_produto(p) for p in hamburgueres]
    )

    lista_chickens = ft.Column(
        controls=[card_produto(p) for p in chickens]
    )

    # --- Navegação entre páginas ---
    def ir_para_home(e):
        page.views.clear()
        page.views.append(view_home())
        page.update()

    def ir_para_hamburgueres(e):
        page.views.append(view_hamburgueres())
        page.update()

    def ir_para_chickens(e):
        page.views.append(view_chickens())
        page.update()

    # --- Views ---
    def view_home():
        return ft.View(
            "/",
            [
                ft.Text("🍔🐒 Orango Tango", size=40, weight="bold"),
                ft.Text("A hamburgueria selvagem que faz seu paladar dançar!", size=18),

                ft.ElevatedButton("Burgers", on_click=ir_para_hamburgueres),
                ft.ElevatedButton("Chickens", on_click=ir_para_chickens),

                ft.Divider(),
                carrinho_text
            ]
        )

    def view_hamburgueres():
        return ft.View(
            "/burgers",
            [
                ft.AppBar(title=ft.Text("🍔 Burgers Orango Tango"), bgcolor=ft.colors.ORANGE),
                lista_hamburgueres,
                ft.ElevatedButton("Voltar", on_click=ir_para_home),
                carrinho_text
            ]
        )

    def view_chickens():
        return ft.View(
            "/chickens",
            [
                ft.AppBar(title=ft.Text("🐔 Chicken Orango Tango"), bgcolor=ft.colors.AMBER),
                lista_chickens,
                ft.ElevatedButton("Voltar", on_click=ir_para_home),
                carrinho_text
            ]
        )

    carrinho_text = ft.Text("Carrinho: 0 itens | Total: R$ 0.00", size=18)

    page.views.append(view_home())


ft.app(target=main, view=ft.WEB_BROWSER)







#codigo main.py do 04 flet fuel
import flet as ft


def main(page: ft.Page):
    def calcular_combustivel(e):
        if not gasolina.value:
           
            gasolina.error_text ="Valor da gasolina não ficar vazio."
            page.update()
        else:
            etanol.error_text =""

            gasolina.value = float(gasolina.value.reaplace(",","."))
            etanol.value = float(etanol.value.reaplace(",","."))
            resultado = "Gasolina" if etanol.value >= gasolina.value*0.7 else "Etanol"
            dlg_modal.content.value = resultado
            gasolina.value =""
            etanol.value =""

            page.open(dlg_modal)

            page.update()

    


    page.title = "App Flex Fuel"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    gasolina = ft.TextField(
        label="Valor da gasolina",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER

    )

    etanol = ft.TextField(
        label= "Valor do etanol" ,
        prefix_text="R$ ",
        keyboard_type= ft.KeyboardType.NUMBER
    )
   
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("melhor abastecer com: "),
        content= ft.text(size=20, weight= "bold"),
        actions= [ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.add (
        ft.SafeArea (
            ft.Container(
                
                alignment=ft.alignment.center,
            ),
            # expand=True
            expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md" : 4, "xl" : 2}),
                ft.Container(etanol, col={"sm": 6, "md" : 4, "xl" : 2})
            ]
            aligmment=ft.MainAxisAlignment.CENTER
        ), 
        ft.Row()
            [
                ft.Container(
                        ft.ElevatedButton("Calcular")
                        padding=30
                )
            ]
    
     )


ft.app(main)