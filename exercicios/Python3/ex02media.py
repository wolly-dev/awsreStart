'''
- Seguimos agora para um exercício clássico de Python. Dada uma lista de números em
Python:
    numeros = [10, 20, 30, 40, 50]
- Calcule a média dos valores dessa lista.
'''

numeros = [10, 20, 30, 40, 50]
soma = sum(numeros)
total = len(numeros)

print(f"O total da soma é {soma}, e a média dessa soma é {soma / total}!")