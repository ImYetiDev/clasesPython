""" Pide al usuario que ingrese tres números y realiza las siguientes operaciones aritméticas con
ellos:

Suma de los tres números.
Resta del tercer número al resultado de la suma de los dos primeros.
Multiplicación de los tres números.
División del primer número entre la suma del segundo y tercer número. Imprime los
resultados. """


num1 = int (input("ingrese primer numero: ") )
num2 = int (input("ingrese segundo numero: ") )
num3 = int (input("ingrese tercer numero: ") )

sum = (num1 + num2 + num3)
res = ((num1 + num2)- num3)
mult = (num1 * num2 * num3)
div = ((num2 + num3)/ num1)

print(f"La suma de los tres numeros es: {sum}")
print(f"La resta del tercer numero al resultado de la suma de los dos primeros es: {res}")
print(f"La multiplicacion de los tres numeros es: {mult}")
print(f"La division del primer numero entre la suma del segundo y tercer numero es: {div}")