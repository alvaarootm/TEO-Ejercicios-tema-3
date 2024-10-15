def imprime_pares_inverso(n):
    for i in range(n if n % 2 == 0 else n - 1, 1, -2):
        print(i, end=" ")
    print()  # Para saltar a la siguiente línea después de imprimir los números

imprime_pares_inverso(4)
imprime_pares_inverso(6)