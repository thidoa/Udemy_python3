from random import randint
numero = str(randint(10000000, 999999999))

novo_cpf = numero
contador = 10
total = 0

for indice in range(19):
    if indice > 8:
        indice -= 9

    total += int(novo_cpf[indice]) * contador

    contador -= 1
    if contador < 2:
        contador = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)

print(novo_cpf)