"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

# Externo
linha = 1
while linha <= qtd_linhas:
    # Interno
    # Ele só sairá deste while, quando coluna <= qtd_colunas for FALSE
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou o laço de repetição!')