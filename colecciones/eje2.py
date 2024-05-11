"""Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas frases. Ejemplo:
f1: hola mundo
f2: como estas
r=["o"]"""

frase_1 = input("Ingrese la primera frase: ")
frase_2 = input("Ingrese la segunda frase: ")

if len(frase_1) == len(frase_2):
    letras = []
    for i in range(len(frase_1)):
        if frase_1[i] == frase_2[i]:
            letras.append(frase_1[i])
    if len(letras) == 0:
        print("No hay letras iguales en la misma posición")
    else:
      print(letras)
else:
    print("Las frases no tienen la misma longitud")