# declaração de dicionário
usuario = {
    'nome': "WalissonRodrigues",
    'nascimento': 16/50/1990,
    'telefone': "(61) 981564692",
    'email': "walisson@gmail.com",
    'endereço': "samambaia"
}

for chave in usuario:
  print(f"{chave.capitalize()}: {usuario[chave]}")

  