print()
print('Texto explicativo.')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2',
        'respostas': {
            'a': '4',
            'b': '3',
            'c': '6',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1',
        'respostas': {
            'a': '0',
            'b': '100',
            'c': '1.5',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4',
        'respostas': {
            'a': '20',
            'b': '1',
            'c': '2',
        },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}?')
    
    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHH! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXIIIII!!! Você ERROU!!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}.')
