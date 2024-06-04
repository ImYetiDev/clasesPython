""" Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad
de frutos recolectados y la cantidad de frutos producidos en total.
Fórmula:
Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100% """


fruta_recogida = int (input("ingrese la cantidad de frutos recolectados: "))
fruta_producida= int (input("ingrese la cantidad de frutos producidos: "))

indice_de_cosecha = (fruta_recogida / fruta_producida) * 100

print ("El indice de cosecha es: " , indice_de_cosecha)
