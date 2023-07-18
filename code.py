import random

# Função para escolher uma palavra aleatória do arquivo "palavras.txt"
def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
        return random.choice(palavras)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_exibida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_exibida += letra + ' '
            else:
                palavra_exibida += '_ '

        print(f"\nPalavra: {palavra_exibida}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        if all(letra in letras_corretas for letra in palavra):
            print("\nParabéns! Você venceu!")
            break

        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra)
            break

        letra = input("\nDigite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra vez.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1

print("Jogo da Forca")
print("Adivinhe a palavra!")
jogo_da_forca()
