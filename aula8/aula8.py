nome = 'Thiago'
idade = 16
altura = 1.69
peso = 49.0
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} e {imc:.2f}')
print(f'{nome} nasceu em {nascimento}.')
