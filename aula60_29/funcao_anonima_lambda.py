lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P1', 8],
]

print(sorted(lista, key=lambda item: item[0], reverse=True))
print(lista)
