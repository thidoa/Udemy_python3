"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-      
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72 
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0                      
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #   
Digito 1 = 0          #   Digito 2 = 9
"""
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
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

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    
    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')