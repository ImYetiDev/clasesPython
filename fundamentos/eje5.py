""" Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad
de frutos recolectados y la cantidad de frutos producidos en total.

Fórmula:
Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100%
 """
 
cantidad_frutos_recolectados = int(input('Ingresa la cantidad de frutos recolectados: '))
cantidad_frutos_producidos = int(input('Ingresa la cantidad de frutos producidos: '))

indice_cosecha = (cantidad_frutos_recolectados / cantidad_frutos_producidos) * 100

print(f'El indice de cosecha es: {indice_cosecha}%')