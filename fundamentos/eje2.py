# Variables: Solicite al usuario que ingrese dos numeros enteros, intercambie los valores de las
#variable sin usar una variable temporal e imprima los valores intercambiados

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

n1 , n2 = n2, n1

print('*Los numeros han sido cambiados*')
print('Primer num: {}'.format(n1), 'Segundo num: {}'.format(n2))