import random

def juego_adivina_numero():
    numero_a_adivinar = random.randint(0, 10)
    oportunidades = 3

    print("¡Bienvenido al juego de adivina el número!")
    print("Tienes 3 oportunidades para adivinar un número entre 0 y 10.")

    for intento in range(1, oportunidades + 1):
        try:
            guess = int(input(f"Intento {intento}: "))
            if guess == numero_a_adivinar:
                print("¡Felicidades! ¡Adivinaste el número!")
                return
            else:
                print("Número incorrecto.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    print(f"Lo siento, has usado todas tus oportunidades. El número era {numero_a_adivinar}.")

if __name__ == "__main__":
    juego_adivina_numero()