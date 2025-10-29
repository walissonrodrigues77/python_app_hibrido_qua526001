# declaração de lista
nomes = [
    "Fulano", 
    "Cicrano", 
    "Beltrano", 
    "João", 
    "Maria", 
    "José"
]

# exibe toda a lista
for nome in nomes:
    print(nome)

# ordena a lista em ordem alfabética
nomes.sort()

# re-exibe a lista em ordem alfabética
print("\nOrdem Alfabética:\n")
for nome in nomes:
    print(nome)

# reverte a ordem da lista
nomes.sort(reverse=True)

print("\nOrdem alfabética reversa:\n")
for nome in nomes:
    print(nome)