'''
- Partindo de uma lista de palavras qualquer, como:
    palavras = ["python", "asimov", "código", "web", "programação"]
- Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista
(em número de caracteres).
'''

nomes = ["Wolly", "Alê", "Victor", "Mista", "Emerson", "Josy", "Kiane", "Larissa", "Preços",
        "Lorena", "Lucas", "Myllena", "Pedro", "Rose", "Samy", "Victoria", "Kássia", "Leandro"]

print(f'O maior nome dessa lista é: {max(nomes, key=len)}.\nO menor nome dessa lista é: {min(nomes, key=len)}.')