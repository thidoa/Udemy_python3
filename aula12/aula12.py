nome = input('Digite o seu primeiro nome: ').strip()

if len(nome) <= 4:
    print('Seu nome e curto!')
elif len(nome) <=6:
    print('Seu nome e normal!')
else:
    print('Seu nome e muito grande!')