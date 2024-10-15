from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    personas = []
    for _ in range(n):
        nombre = input("Introduce el nombre: ")
        edad = int(input("Introduce la edad: "))
        personas.append(Persona(nombre, edad))
    return personas

def edad_media(personas):
    if not personas:
        return 0  # Manejar caso de lista vacía
    total_edad = sum(persona.edad for persona in personas)
    return total_edad / len(personas)

def mayores_18(personas):
    mayores = [persona.nombre for persona in personas if persona.edad >= 18]
    return sorted(mayores)

def edades_distintas(personas):
    edades = sorted(set(persona.edad for persona in personas))
    return edades

def persona_mas_joven(personas):
    if not personas:
        return None  # Manejar caso de lista vacía
    return min(personas, key=lambda persona: persona.edad).nombre

# Prueba de las funciones
n = 3
personas = lee_personas(n)
print("\nLista de personas:", personas)

# Calculando la edad media
media = edad_media(personas)
print("Edad media:", media)

# Nombres de mayores de 18
nombres_mayores = mayores_18(personas)
print("Personas mayores de 18:", nombres_mayores)

# Edades distintas
edades = edades_distintas(personas)
print("Edades distintas:", edades)

# Persona más joven
joven = persona_mas_joven(personas)
print("Persona más joven:", joven)
