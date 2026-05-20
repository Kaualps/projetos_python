import random
palavras = ["ESTRUTURA", "COMPUTADOR", "TABLET", "TELEVISÃO", "PROJETOR", "DOUTOR", "CAMA"]
palavra = random.choice(palavras)
letras_acertadas = []
tentativas = 6
while tentativas > 0:
    letra = input("Digite uma letra: ").upper()
    if letra in palavra:
        letras_acertadas.append(letra)
    else:
        tentativas -= 1
    palavra_mostrada = ""
    for letra_palavra in palavra:
        if letra_palavra in letras_acertadas:
            palavra_mostrada += letra_palavra
        else:
            palavra_mostrada += "_"
    print(palavra_mostrada)
    if palavra_mostrada == palavra:
        print("Parabéns! Você acertou a palavra!")
        break
else:
    print("Você perdeu! A palavra era:", palavra)