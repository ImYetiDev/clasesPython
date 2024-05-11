""" Pregunte al usuario cuántos elementos desea ingresar en una lista, luego solicite cada uno de ellos y presente el contenido de la lista y su
contenido invertido """

n = int(input('¿Cuántos elementos desea ingresar en la lista? '))

lista = []

for i in range(n):
    lista.append(input(f'Ingrese el elemento {i+1}: '))
    
print(f'La lista ingresada es: {lista}')
#Usando el operador slicing de Python, podemos invertir la lista de la siguiente manera:
print(f'La lista invertida es: {lista[::-1]}')