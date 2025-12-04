import flet as ft
import random
import time

def gerar_baralho():
    naipes = ["♠","♥","♦","♣"]
    valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    baralho = [v+n for n in naipes for v in valores]
    random.shuffle(baralho)
    return baralho

def cor_carta(c):
    return "red" if c.endswith("♥") or c.endswith("♦") else "white"

def valor_carta(c):
    v = c[:-1]
    if v=="A": return 1
    if v=="J": return 11
    if v=="Q": return 12
    if v=="K": return 13
    return int(v)

def main(page: ft.Page):
    page.title="Paciência Antiga"
    page.bgcolor="#222222"
    page.window_width=700
    page.window_height=900

    baralho=[]
    colunas=[]
    fundamentos={"♠":[],"♥":[],"♦":[],"♣":[]}
    selecionada={"col":None,"idx":None}
    pontos=0
    inicio=time.time()

    col_views=[ft.Column() for _ in range(7)]
    fund_views={n:ft.Column() for n in "♠♥♦♣"}
    msg=ft.Text("",color="yellow")
    score_text=ft.Text("",color="white")
    timer_text=ft.Text("",color="white")

    def atualizar():
        # Atualiza colunas
        for i in range(7):
            col_views[i].controls.clear()
            if len(colunas[i])==0:
                col_views[i].controls.append(
                    ft.Container(content=ft.Text("(vazio)",color="white"),
                                 bgcolor="#333333",width=80,height=30)
                )
            else:
                for idx,carta in enumerate(colunas[i]):
                    txt=carta["valor"] if carta["virada"] else "▒▒▒"
                    cor=cor_carta(carta["valor"]) if carta["virada"] else "white"
                    is_sel=(selecionada["col"]==i and selecionada["idx"]==idx)
                    borda="#00FFAA" if is_sel else "#FFFFFF"

                    def make_press(i=i,idx=idx):
                        return lambda e: click_carta(i,idx)

                    col_views[i].controls.append(
                        ft.Container(
                            content=ft.Button(txt,on_click=make_press(),
                                              bgcolor="#FFAA33" if carta["virada"] else "#555555",
                                              color=cor),
                            padding=5,
                            width=80,
                            height=30
                        )
                    )

        # Atualiza fundamentos
        cores_fund={"♠":"#00FFFF","♥":"#FF5555","♦":"#FFAAFF","♣":"#55FF55"}
        for n in "♠♥♦♣":
            fund_views[n].controls.clear()
            if fundamentos[n]:
                fund_views[n].controls.append(
                    ft.Container(content=ft.Text(fundamentos[n][-1]["valor"],color=cor_carta(fundamentos[n][-1]["valor"])),
                                 bgcolor=cores_fund[n],width=60,height=30)
                )
            else:
                fund_views[n].controls.append(
                    ft.Container(content=ft.Text(n,color="white"),
                                 bgcolor="#333333",width=60,height=30)
                )

        # Atualiza pontos e timer
        score_text.value=f"Pontos: {pontos}"
        timer_text.value=f"Tempo: {int(time.time()-inicio)}s"

        # Mensagem de vitória
        if all(len(fundamentos[n])==13 for n in "♠♥♦♣"):
            msg.value="🎉 Parabéns! Você venceu!"
        else:
            msg.value=""

        page.update()

    def click_carta(col,idx):
        nonlocal pontos
        carta=colunas[col][idx]
        if not carta["virada"]:
            carta["virada"]=True
            atualizar()
            return
        if selecionada["col"] is None:
            selecionada["col"]=col
            selecionada["idx"]=idx
            atualizar()
            return
        if selecionada["col"]==col and selecionada["idx"]==idx:
            selecionada["col"]=None
            selecionada["idx"]=None
            atualizar()
            return
        mover_carta(selecionada["col"],selecionada["idx"],col,idx)
        selecionada["col"]=None
        selecionada["idx"]=None
        atualizar()

    def mover_carta(orig_col,orig_idx,dest_col,dest_idx):
        nonlocal pontos
        carta=colunas[orig_col][orig_idx]
        if dest_idx==len(colunas[dest_col])-1 or len(colunas[dest_col])==0:
            if len(colunas[dest_col])==0 or (colunas[dest_col][-1]["virada"] and
               valor_carta(colunas[dest_col][-1]["valor"])==valor_carta(carta["valor"])+1 and
               cor_carta(colunas[dest_col][-1]["valor"])!=cor_carta(carta["valor"])):
                colunas[dest_col].append(carta)
                del colunas[orig_col][orig_idx]
                pontos+=5
                return
        n=carta["valor"][-1]
        if (not fundamentos[n] and carta["valor"][:-1]=="A") or (fundamentos[n] and valor_carta(carta["valor"])==valor_carta(fundamentos[n][-1]["valor"])+1):
            fundamentos[n].append(carta)
            del colunas[orig_col][orig_idx]
            pontos+=10

    def novo_jogo(e=None):
        nonlocal baralho,colunas,fundamentos,selecionada,pontos,inicio
        baralho=gerar_baralho()
        colunas=[]
        for _ in range(7):
            pilha=[{"valor":baralho.pop(),"virada":False} for _ in range(5)]
            colunas.append(pilha)
        fundamentos={"♠":[],"♥":[],"♦":[],"♣":[]}
        selecionada={"col":None,"idx":None}
        pontos=0
        inicio=time.time()
        atualizar()

    def comprar(e):
        if baralho:
            nova={"valor":baralho.pop(),"virada":True}
            colunas[0].append(nova)
        atualizar()

    # Botões
    novo_btn=ft.Button("Novo Jogo",on_click=novo_jogo,bgcolor="#00D46A",color="black")
    comprar_btn=ft.Button("Comprar Carta",on_click=comprar,bgcolor="#00A3FF",color="black")

    # Layout
    page.add(
        ft.Text("PACIÊNCIA ANTIGA",color="#00FFD5"),
        ft.Row([fund_views[n] for n in "♠♥♦♣"]),
        ft.Row([col_views[i] for i in range(7)]),
        ft.Row([novo_btn,comprar_btn,score_text,timer_text]),
        msg
    )

    novo_jogo()

if __name__=="__main__":
    ft.app(target=main)
