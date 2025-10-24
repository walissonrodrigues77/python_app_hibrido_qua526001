#Crie um programa que recebe do usuário o nome e a idade,
# e em seguida, exiba na tela uma lista de filmes, 
# suas respectivas salas e classificações indicativas:
#ala 1 - A Roda Quadrada - Livre
#Sala 2 - A Volta dos Que Não Foram - 12 anos
#Sala 3 - Poeira em Alto Mar - 14 anos
# Sala 4 - As Tranças do Rei Careca - 16 anos
#Sala 5 - A Vingança do Frango Assado - 18 anos

#O usuário deverá escolher o filme, 
# e caso ele tiver a idade mínima para ver o filme,
#  imprime o ingresso e encerra o programa. 
# Caso o usuário não tenha a idade mínima, 
# o programa impede a entrada do usuário e re-exibe a lista de filmes 
# para que o mesmo escolha outro filme.



def main():
    # Solicita o nome e idade do usuário
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    # Lista de filmes e suas classificações
    filmes = [
        {"sala": 1, "titulo": "A Roda Quadrada", "classificacao": "Livre"},
        {"sala": 2, "titulo": "A Volta dos Que Não Foram", "classificacao": "12 anos"},
        {"sala": 3, "titulo": "Poeira em Alto Mar", "classificacao": "14 anos"},
        {"sala": 4, "titulo": "As Tranças do Rei Careca", "classificacao": "16 anos"},
        {"sala": 5, "titulo": "A Vingança do Frango Assado", "classificacao": "18 anos"},
    ]

    while True:
        # Exibe a lista de filmes
        print("\nEscolha um filme:")
        for filme in filmes:
            print(f"Sala {filme['sala']} - {filme['titulo']} - Classificação: {filme['classificacao']}")

        # Solicita a escolha do filme
        escolha = int(input("\nDigite o número da sala do filme que deseja assistir: "))

        # Verifica se a escolha é válida
        if 1 <= escolha <= 5:
            filme_escolhido = filmes[escolha - 1]
            classificacao = filme_escolhido["classificacao"]

            # Verifica se o usuário tem a idade mínima para o filme
            if (classificacao == "Livre" or
                (classificacao == "12 anos" and idade >= 12) or
                (classificacao == "14 anos" and idade >= 14) or
                (classificacao == "16 anos" and idade >= 16) or
                (classificacao == "18 anos" and idade >= 18)):
                
                # Exibe o ingresso
                print(f"\nIngresso aprovado! {nome}, você pode assistir '{filme_escolhido['titulo']}' na Sala {filme_escolhido['sala']}.")
                break
            else:
                # Usuário não tem idade mínima para o filme
                print(f"\nDesculpe, {nome}. Você não tem idade suficiente para assistir '{filme_escolhido['titulo']}'.")
        else:
            print("\nEscolha inválida! Tente novamente.")

if __name__ == "__main__":
    main()