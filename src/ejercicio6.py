def calcula_precios(precio_normal, edades):
    precios = []
    for edad in edades:
        if edad <= 18 or edad >= 65:
            precios.append(precio_normal * 0.5)  # Precio reducido
        else:
            precios.append(precio_normal)  # Precio normal
    return precios

precio_normal = 6
edades = [8, 18, 25, 44, 64, 65, 70]

precios = calcula_precios(precio_normal, edades)
print(f"Precios de las entradas para personas con edades {', '.join(map(str, edades))} (precio normal de la entrada: {precio_normal}€):")
print(", ".join(map(str, precios)))
