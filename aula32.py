"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input(
#     'Digite um número: '
#     )
# try:
#     num_int = int(numero)
#     if num_int % 2 == 0:
#         print(f'O número {num_int} é par.')
#     else:
#         print(f'O número {num_int} é ímpar.')
# except:
#     print('Não é um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input(
#     'Digite um horário: '
# )
# try:
#     hora_float = float(hora)
#     if 0 <= hora_float <= 11:
#         print('Bom dia.')
#     elif 12 <= hora_float <= 17:
#         print('Boa tarde.')
#     else:
#         print('Bom noite.') 
# except:
#     print('Não é uma hora!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input(
    'Escreva seu nome: '
)
try:
    if not nome.isalpha():
        print('Por favor, digite o nome válido (sem números).')
    elif len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) <= 6:
        print('Seu nome é normal.')
    else: 
        print('Seu nome é grande.')
except:
    print('Nome inválido!')