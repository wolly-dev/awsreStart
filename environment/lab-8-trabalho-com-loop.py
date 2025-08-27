import random
print("Bem vindo ao jogo 'Adivinhe o Numero'!")
print("As regras sao simples. Eu pensarei num numero e voce tentara adivinhar.")
number = random.randint(1, 10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Adivinhe um numero entre 1 e 10: ")
    if int(guess) == number:
        print(f"Voce chutou {guess}. Esta correto! Voce venceu!")
    else:
        print(f"Voce chutou {guess}. Desculpe, mas nao esta correto. Tente novamente!")