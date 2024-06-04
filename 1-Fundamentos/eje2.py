""" Variables: Solicite al usuario que ingrese dos numeros enteros, intercambie los valores de las
variable sin usar una variable temporal e imprima los valores intercambiados """

num1 = int (input("Ingrese un numero entero: "))
num2 = int (input("Ingrese otro numero entero: "))

num1,num2 = num2,num1

print (f'Numero 1 cambiado por Numero 2: {num1}')
print (f'Numero 2 cambiado por Numero 1: {num2}')