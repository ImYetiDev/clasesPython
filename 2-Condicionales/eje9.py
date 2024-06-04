import random

print("Ingrese 6 números para jugar a la lotería:")
numero1 = int(input("Ingrese el número 1: "))
numero2 = int(input("Ingrese el número 2: "))
numero3 = int(input("Ingrese el número 3: "))
numero4 = int(input("Ingrese el número 4: "))
numero5 = int(input("Ingrese el número 5: "))
numero6 = int(input("Ingrese el número 6: "))
numeros_usuario = [numero1, numero2, numero3, numero4, numero5, numero6]

numeros_loteria = random.sample(range(1, 51), 6)

coincidencias = len(set(numeros_usuario).intersection(numeros_loteria))


print("Los números de la lotería son:", numeros_loteria)
print(f"Ha acertado {coincidencias} números.")


if coincidencias == 6:
    print("¡Felicidades! Ha ganado el premio mayor.")
elif coincidencias >= 3:
    print("Ha ganado un premio menor.")
else:
    print("No has ganado ningún premio.")
  


    
    
