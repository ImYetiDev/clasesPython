""" Solicita al usuario que ingrese una secuencia de números separados por comas. Cuenta
cuántos números pares e impares hay en la secuencia """

numeros = input("Ingrese una secuencia de numeros separados por comas: ")
numeros = numeros.split(",")

pares = 0
impares = 0

for numero in numeros:
    if int(numero) % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Impares:", impares)
