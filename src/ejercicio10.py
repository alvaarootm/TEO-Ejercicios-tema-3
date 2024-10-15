from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


def autores_disponibles(libros, inicial):
    autores = {libro.autor for libro in libros if libro.disponible and libro.autor.startswith(inicial)}
    return sorted(autores)

def titulos_baratos_actuales(libros):
    return [libro.titulo for libro in libros if libro.precio < 20 and libro.fecha_publicacion.year >= 2001]

def media_precios(libros, palabra):
    precios = [libro.precio for libro in libros if palabra.lower() in libro.titulo.lower()]
    if not precios:
        return None
    return sum(precios) / len(precios)

def libro_mas_reciente(libros):
    return max(libros, key=lambda libro: libro.fecha_publicacion)



if __name__ == "__main__":
    libros = lee_libros("data/libreria.csv")
    print(f"Se han leído {len(libros)} libros.")

    print("Autores disponibles:", autores_disponibles(libros, "M"))
    print("Titulos baratos actuales:", titulos_baratos_actuales(libros))
    print(
        "Media de precios de libros con la palabra 'El':", media_precios(libros, "El")
    )
    print("Libro más reciente:", libro_mas_reciente(libros))
