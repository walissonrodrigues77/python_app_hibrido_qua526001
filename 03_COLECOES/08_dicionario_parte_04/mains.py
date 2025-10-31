#TODO - declaração de coleções
#criar um programa com varios usuarios 
#lista com varios dados diferentes 
#cada lista deve virar dicionarios


usuarios = [
{
    'nome':"fulanos",
    'idade':20, 
    'email':"fulano@gmail.com"
}
{
    'nome': "cricrano",
    'idade':25, 
    'email': "cricrano@gmail.com"
}
{ 
    'nome':"beltrano",
    'idade':30, 
    'email':"beltrano@gmail.com"

}
]
#exibindo os dados dos usuarios
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}:{usuario[chave]}")
