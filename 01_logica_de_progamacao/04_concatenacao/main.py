# declaração de variáveis
nome = "Alex Machado"
idade = 40

# concatenação de valores
# forma 1
print("Boa tarde, meu nome é " + nome + " e tenho " + str(idade) + " anos.")
# forma 2
print("Boa tarde, meu nome é", nome, "e tenho", idade, "anos.")
# forma 3
print("Boa tarde, meu nome é {} e tenho {} anos.".format(nome, idade))
# forma 4 (mais usada) f-string
print(f"Boa tarde, meu nome é {nome} e tenho {idade} anos.")