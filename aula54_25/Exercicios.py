"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def saudacao(saudacao='Olá', nome='Usuário'):
    return saudacao, nome

print(saudacao('Yae', 'Thiago'))

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
def soma(numero1, numero2, numero3):
    return numero1+numero2+numero3

print(soma(2, 4, 8))

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo percentual (ex.10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def percentual(numero, percentual):
    resultado = (numero/100) * (100 + percentual)
    return resultado

print(percentual(200, 10))

"""
4 - Fizz Buzz - Se o parâmetro  da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retrone buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, no caso contrario, retorne o número enviado.
"""

def fizzbuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
         
    return numero

print(fizzbuzz(3))
