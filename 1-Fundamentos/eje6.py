""" Pide al usuario que ingrese una frase y un carácter. Luego, cuenta cuántas veces aparece ese
carácter en la frase e imprime el resultado. """

frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter: ")

contador = 0
for i in frase:
    if i == caracter:
        contador += 1
print(f"El caracter {caracter} aparece {contador} veces en la frase.")