"""
Iterando strings com while
"""
#.........01234567 (+)
# nome = 'Isabele'  # Iteráveis
#.........7654321 (-)


nome = 'Isabele'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)