nombres = ["Juan", "Ana", "Manuel", "Irene", "Jaime", "María"]
apellidos = ["Ruiz", "López", "Martínez", "Fernández", "Jiménez", "Castro"]

nombres_completos = []

for nombre, apellido in zip(nombres, apellidos):
    nombres_completos.append(f"{nombre} {apellido}")

print(nombres_completos)
