def indica_primera_aparicion(lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return -1

lista = ["árbol", "coche", "casa", "peatón"]
valor1 = "casa"
valor2 = "bicicleta"

print(f'Posición de "{valor1}" en la lista {lista}: {indica_primera_aparicion(lista, valor1)}')
print(f'Posición de "{valor2}" en la lista {lista}: {indica_primera_aparicion(lista, valor2)}')
