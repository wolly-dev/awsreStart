myString = 'Essa é a minha string'
print(myString)
print(type(myString))

firstString = 'cacho'
secondString = 'eira'
thirdString = firstString + secondString
print(thirdString)

name = input('Qual o seu nome? ')
print(name)

color = input('Qual sua cor favorita? ')
animal = input('Qual seu animal favorito? ')
#format antigo, eca
#print("{}, vocë gosta de {} {} !".format(name, color, animal))
#jeito novo e mais top abaixo
print(f'{name}, você gosta de {animal} {color}!')