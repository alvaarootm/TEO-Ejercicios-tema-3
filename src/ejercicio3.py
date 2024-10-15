def imprime_pares(n):
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    print()  # Para saltar a la siguiente línea después de imprimir los números

imprime_pares(4)
imprime_pares(6)