""" . Solicita al usuario que ingrese un número y calcula la suma de los factoriales de los números
del 1 al número ingresado """

num = int(input("Ingrese un numero: "))

factorial = 1
suma = 0

for i in range(1, num + 1):
    factorial *= i
    suma += factorial
    
print("La suma de los factoriales de los numeros del 1 al", num, "es:", suma)