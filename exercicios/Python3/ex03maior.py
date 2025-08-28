'''
- Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do
mês de dois amigos, João e Pedro. Cada valor na lista representa o gasto em uma das
semanas do mês:

    gastos_joao = [300, 500, 200, 800]
    gastos_pedro = [200, 400, 500, 700]

- Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro.
Para isso, crie um código em Python que responda a essa pergunta.
'''

joaoGastos = [300, 500, 200, 800]
pedroGastos = [200, 400, 500, 700]

joaoSoma = sum(joaoGastos)
pedroSoma = sum(pedroGastos)

if joaoSoma > pedroSoma:
    print("João, aprende a fechar essa carteira!")
elif pedroSoma > joaoSoma:
    print("Caraca Pedro, ta pensando que é rico?")
else:
    print("Os dois conseguiram a proeza de gastar a mesma quantia de 1800...")