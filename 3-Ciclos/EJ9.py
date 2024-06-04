"""  Elabore un algoritmo utilizando el ciclo While que permita simular un temporizador simple que
cuenta hacia atras desde un número ingresado por el usuario hasta 0. """

num = int(input("Ingrese cuandos segundos desea: "))

while num > 0:
    print(num)
    num = num - 1
print("Gracias por usar")