#codigo main.py do 04 flet fuel
import flet as ft


def main(page: ft.Page):
    page.fonts = {
        "Poppins": "https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJLucHtAOvWDSA.woff2"
    }

    page.theme = ft.Theme(font_family="Poppins")
    page.title = "App Flex Fuel"
    page.theme_mode = ft.ThemeMode.LIGHT



    def calcular_combustivel(e):
        if not gasolina.value:
           
            gasolina.error_text ="Valor da gasolina não ficar vazio."
            page.update()
        else:
            etanol.error_text =""

            gasolina.value = float(gasolina.value.replace(",","."))
            etanol.value = float(etanol.value.replace(",","."))
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
        title=ft.Text(" 👇 Melhor ⛽Abastecer com: " ),
        content= ft.Text(size=20, weight= "bold"),
        actions= [ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [

                    ft.Container(
                        ft.Text("🚗  FLEX ⛽ FUEL  🏍", size=55, weight="bold"),      
                        alignment=ft.alignment.center,            
                        padding=100

                    )
                    ft.Container(
                        ft.Image(
                            src= "nome imagem.jpeg",
                            fit=ft.CONTAIN
                            erro_content=ft.Text("Não possivel carregar imagem"),
                    ),
                    alignment=ft.alignment.center

                ),
            ]
        )
            
    ),

         ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md" : 4, "xl" : 2}),
                ft.Container(etanol, col={"sm": 6, "md" : 4, "xl" : 2})
            ],
        alignment=ft.MainAxisAlignment.CENTER
        
        ), 
        ft.Row(
            [
                ft.Container(
                            
                        ft.ElevatedButton("👉Calcular", on_click=calcular_combustivel,
                        style=ft.ButtonStyle(
                        
                            padding=35,
                        text_style=ft.TextStyle(size=25, weight="bold")
                        
                        ),
                        
                        
                    )    
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
     )


ft.app(target=main)
