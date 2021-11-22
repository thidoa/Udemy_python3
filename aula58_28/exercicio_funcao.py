"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""
def principal(funcao):
    return funcao()

def ola_mundo():
    return 'ola mundo!'

executando = principal(ola_mundo)
print(executando)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

rodando = mestre(fala_oi, 'Thiago')
print(rodando)

rodando2 = mestre(saudacao, 'Thiago', 'Yaee')
print(rodando2)