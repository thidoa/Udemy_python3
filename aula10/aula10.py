numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('O numero e par!')
    else:
        print('O numero e impar!')
else:
    print('Nao e um numero inteiro')