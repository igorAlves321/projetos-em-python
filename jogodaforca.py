import random
import time
palavras = ['pato', 'livro', 'panela','abacate','bola', 'telefone', 'carro', 'computador']
palavra_secreta = random.choice(palavras).lower() # transforma em minúscula
letras_escolhidas_pela_pessoa = []
tentativas = 6

print('='*20)
print("JOGO DA FORCA!")
print('='*20)
print("jogo da forca! Vamos jogar?")
jogar = str(input("Sim ou Não: ")).strip().upper()

if jogar in 'SIM':
    print("Voce tem 6 chances para acertar a palavra! Se não acertar voce ja sabe o que acontece, certo?")
    print("\033[31mPensando em palavra...")
    time.sleep(3)
    print("\033[30mPalavra escolhida com sucesso!")


else:
    print("Ate a proxima!")
    exit()



# gera a lista de underlines, com o tamanho da palavra escolhida
palpites = ['_'] * len(palavra_secreta)
print(" A palavra tem {} letras".format(len(palavra_secreta)))
print(' '.join(palpites)) # mostra os underlines separados por espaço

while True:
    print("Qual letra voce acha que a palavra tem? ")
    while True:
        letra = input("Letra:").lower() # transforma em minúscula
        if len(letra) != 1:
            print('Digite apenas uma letra')
        else:
            if letra in letras_escolhidas_pela_pessoa:
                print('A letra {} já foi escolhida'.format(letra))
            else:
                break

    letras_escolhidas_pela_pessoa.append(letra)
    print('letras tentadas: {}'.format((' ').join(letras_escolhidas_pela_pessoa)))

    if letra in palavra_secreta: #apartir dessa linha
        posicoes = []
        # verifica todas as posições que tem a letra
        for i, c in enumerate(palavra_secreta):
            if letra == c:
                palpites[i] = c
                posicoes.append(i) #ate essa linha
        print("Você acertou uma letra nas posições {}".format(', '.join(map(str, posicoes)))) #map converte para qualquer coisa
        print(' '.join(palpites))
        if palavra_secreta == ''.join(palpites):
            print('Parabens voce ganhou!')
            break
    else:
        print("Voce errou uma letra :(")
        tentativas -= 1
        if tentativas <= 0:
            print("Você foi inforcado")
            print("A palavra era {}".format(palavra_secreta))
            break
        print("Tente novamente.\nAgora você tem {} chances".format(tentativas))

print("Ate a proxima!")