# Todo: atividade 
#crie uma lista com os nome de todos os estados brasileiros, e mostre na tela os estados em ordem alfabética.

# Lista com todos os estados brasileiros
estados = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

# Ordena a lista em ordem alfabética
estados.sort()

# Mostra os estados em ordem alfabética
print("\nEstados brasileiros em ordem alfabética:\n")
for i, estado in enumerate(estados, start=1):
    print(f"\n{i}. {estado}")

# Solicita que o usuário escolha um estado pelo número
print("\nDigite o número do estado que você deseja ver:")
numero = int(input("Número: "))

# Verifica se o número é válido
if 1 <= numero <= len(estados):
    print(f"\nVocê escolheu: {estados[numero - 1]}")
else:
    print("\nNúmero inválido! Tente novamente.")