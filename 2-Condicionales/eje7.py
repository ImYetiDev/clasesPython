import random

numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)

suma = numero1 + numero2

print("La suma de los dos números es:", suma)

adivina1 = int(input("Adivina el primer número: "))
adivina2 = int(input("Adivina el segundo número: "))

if adivina1 == numero1 and adivina2 == numero2:
    print("¡Felicidades! Adivinaste los números .")
elif adivina1 == numero2 and adivina2 == numero1:
    print("¡Felicidades! Adivinaste los números en diferente orden.")
else:
    print("Lo siento, no adivinaste los números.")
    print("Los números originales eran:", numero1, "y", numero2)
