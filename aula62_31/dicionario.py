# OBS.: Chaves tem que ser únicas 

# ADICIONAR CHAVE NO DICIONÁRIO 

d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave' # adicionando nova chave...

print(d1) # {'chave1': 'valor da chave', 'nova_chave': 'Valor da nova chave'}

# ACESSAR UMA CHAVE   
print(d1['chave1']) # valor da chave 

# VALORES DE CHAVES PRECISA SER IMUTÁVEL
d2 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}

d2['naoexiste'] = 'Agora existe.'

if d2.get('naoexiste') is not None:
    print(d2.get('naoexiste'))

print('OI') # Agora existe
            # OI

# ACESSAR OS VALORES

d3 = {
    'chave1' : 'valor',
    'chave2' : 'Outro valor',
    'chave3' : 'Tupla',
}

for v in d3.values(): # acessando valores...
    print(v) # valor
             # Outro valor
             # Tupla

for k, v in d1.items():
    print(k, v) # chave1 valor
                # chave2 Outro valor
                # chave3 Tupla

# CRIAR CÓPIA DE UM DICIONÁRIO

d4 = {1: 'a', 2: 'b', 'c' : ['Luiz', 'Otávio']}
v = d4.copy() # Criando uma shalowcopy(cópa raza)

v[1] = 'Luiz'
v['c'][0] = 'Joãozinho'

print(d4) # {1: 'a', 2: 'b', 'c': ['Joãozinho', 'Otávio']}
print(v)  # {1: 'Luiz', 2: 'b', 'c': ['Joãozinho', 'Otávio']}

# CRANDO UMA CÓPIA PROFUNDA

import copy

d5 = {1: 'a', 2: 'b', 'c' : ['Luiz', 'Otávio']}
t = copy.deepcopy(d5)

t[1] = 'Luiz'
t['c'][0] = 'Joãozinho'

print(d5) # {1: 'a', 2: 'b', 'c': ['Luiz', 'Otávio']}
print(t)  # {1: 'Luiz', 2: 'b', 'c': ['Joãozinho', 'Otávio']}


# CONCATENAR DICIONÁROS

d12 = {
    1: 2,
    2: 3,
    4: 5,
}

d22 = {
    'a' : 'b',
    'c' : 'd',
}
d12.update(d22) # concatenando...
print(d12) # {1: 2, 2: 3, 4: 5, 'a': 'b', 'c': 'd'}