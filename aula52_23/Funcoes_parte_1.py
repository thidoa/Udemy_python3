"""
Funções - def em Python (Parte 1)
"""
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)
