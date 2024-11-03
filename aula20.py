primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(
        f"primero_valor='{primeiro_valor}'"
        f"é maior que o segundo_valor='{segundo_valor}'."
        # rf'primero_valor=\'{primeiro_valor}\'.' -> Com escape simples
        # rf"é maior que o segundo_valor=\"{segundo_valor}\"." -> Com escape dupla
        f"é maior que o segundo_valor='{segundo_valor}'."
        )

elif segundo_valor > primeiro_valor:
    print(
        f"segundo_valor='{segundo_valor}'"
        f"é maior que o primeiro_valor='{primeiro_valor}'."
        )

else:
    print("Valores são iguais!")