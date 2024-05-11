""" Pide al usuario que ingrese tres números y realiza las siguientes operaciones aritméticas con
ellos:
Suma de los tres números.
Resta del tercer número al resultado de la suma de los dos primeros.
Multiplicación de los tres números.
División del primer número entre la suma del segundo y tercer número. Imprime los
resultados. """

n1 = int(input('Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))
n3 = int(input('Ingresa el tercer numero: '))

suma = n1 + n2 + n3
resta = (n1 + n2) - n3
multi = n1 * n2 * n3
div = (n2 + n3) / n1

print(f'El resultado de la suma es: {suma}')
print(f'El resultado de la resta es: {resta}')
print(f'El resultado de la multiplicacion es: {multi}')
print(f'El resultado de la division {div}')