import random
import os
lista_nome = []
lista_sorteados = []

while True:
    nome = input("Digite os nomes que serão sorteados:")
    if nome != "":
        # O append adiciona o que foi digitado dentro do nome, dentro da lista.
        lista_nome.append(nome)

    else:
        break

while True:
    if lista_nome:
        os.system('cls')  
        escolhido = random.choice(lista_nome)
        lista_sorteados.append(escolhido)
        print(f'O sorteado é {escolhido}')
        opcao=input('Deseja sortear outro nome?(s/n)').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Não existe nomes para ser sorteados')
        break




print('Programa finalizado.')
print(f'Lista dos nomes: {lista_nome}')
print(f'Lista dos sorteados: {lista_sorteados}')