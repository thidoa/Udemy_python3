"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é penta.'
lista = string.split(' ')
print(lista)

print('---------------------')

for indice, valor in enumerate(lista):
    print(indice, valor)

print('---------------------')

lista2 = ' '.join(lista)
print(lista2)
