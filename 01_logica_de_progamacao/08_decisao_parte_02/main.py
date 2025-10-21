# declaracao de variaveis
nome = input("informar o nome:").strip().title()
idade = int(input("informar a idade:").strip)
altura = float(input("informar a altura: ").strip().replace(",","."))
if idade >= 12 and altura >= 1.15:
     print(f"entrada de {nome} autorizada.")
else:
    print(f"entrada de {nome} não autorizada")
