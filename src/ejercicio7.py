import random

def juego_adivina_numero(maximo, max_intentos):
    numero_a_adivinar = random.randint(1, maximo)
    intentos = 0

    print(f"Adivina el número entre 1 y {maximo}. Tienes {max_intentos} intentos.")

    while intentos < max_intentos:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1

            if intento < 1 or intento > maximo:
                print(f"Por favor, introduce un número entre 1 y {maximo}.")
                continue

            if intento < numero_a_adivinar:
                print("El número a adivinar es mayor.")
            elif intento > numero_a_adivinar:
                print("El número a adivinar es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intentos} intentos.")
                return

        except ValueError:
            print("Por favor, introduce un número válido.")

    print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_a_adivinar}.")

juego_adivina_numero(100, 10)
