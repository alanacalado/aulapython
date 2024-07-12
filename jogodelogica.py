import random

palavras = ['python', 'openai', 'programação','tecnologia','desenvolvedor','garoto de programa','algoritmo','software','computador','programas']

palavra_secreta = random.choice(palavras)
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_escondida = ''
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_escondida += letra 
        else:
            palavra_escondida += '_'

    print('Palavra:', palavra_escondida)
    print('Letras erradas:', letras_erradas)
    print('Tentativas restantes:', tentativas)

    if palavra_escondida == palavra_secreta:
        print('Parabéns! Você venceu!✪ ω ✪')
        break
    elif tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)
        break

    letra_usuario = input('Digite uma letra:').lower()

    if letra_usuario in palavra_secreta:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        letras_erradas.append(letra_usuario)
        tentativas -= 1
