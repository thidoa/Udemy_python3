# add (adicionar), update (atualizar), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_diference ^ (Elementos que estão nos dois sets, mas não em ambos)
s1 = {1,2,3,4,5}

for v in s1:
    print(v)

s2 = set() # Criando um set vazio
# Adicionando elementos ao set
s2.add(1)
s2.add(2)

s2.discard(2) # Removendo o elemento 2 do set
s2.update([4,5,6,7]) # Adiciona elementos ao set interando ele 

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9,'Luiz', 'Luiz']
l1 = set(l1)

print(l1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'Luiz'}

s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4 # Unindo os sets

print(s5) # {1, 2, 3, 4, 5, 6}

s6 = {1,2,3,4,5}
s7 = {1,2,3,4,5,6}
s8 = s6 & s7 # interseção dos sets

print(s8) # {1, 2, 3, 4, 5}