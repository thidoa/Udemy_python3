nome = 'Thiago'
idade = 16  # int
altura = 1.69  # float
e_maior = idade > 18
peso = 49
imc = peso / altura**2

print(nome, 'tem', idade, 'anos de idade e seu imc e', imc)
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
print('{im} tem {n} anos de idade e seu imc e {id:.2f}'.format(n=nome, id=idade, im=imc))
