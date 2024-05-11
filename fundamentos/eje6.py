"""Manipulación de Cadenas:
Pide al usuario que ingrese una frase y un carácter. Luego, cuenta cuántas veces aparece ese
carácter en la frase e imprime el resultado.
 """
 
frase = input('Ingresa una frase: ')
caracter = input('Ingresa un caracter: ')

contador = frase.count(caracter)

print(f'El caracter {caracter} aparece {contador} veces en la frase.')