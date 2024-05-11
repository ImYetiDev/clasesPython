"""Leer una frase y almacenar en una tupla la frase leída pero sin espacios. Mostrar el contenido de la tupla """

frase = input("Ingrese una frase: ")
tupla = tuple(frase.replace(" ", ""))
print(tupla)