#
#userReply = input('Você precisa enviar um pacote? (Digite sim ou não) ')
#if userReply == "sim":
#    print('Nós podemos te ajudar com o envio do pacote!')
#else:
#    print('Por favor, nos procure quando você precisar de um pacote enviado. Obrigado!')
    
userReply = input("Você gostaria de comprar estampas, envelope ou fazer cópia? (Digite estampas, envelope ou copia.) ")
if userReply == "estampas":
    print("Nós temos muitos designs de estampas disponíveis.")
elif userReply == "envelope":
    print("Nós temos muitos tamanhos de envelopes disponíveis.")
elif userReply == "copia":
    copies = input("Quantas cópias voce gostaria? (Digite um numero) ")
    print(f"Aqui estao {copies} copias")
else:
    print("Obrigado. Por favor, volte novamente!.")