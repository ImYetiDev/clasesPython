'''
Realiza una función que reciba un número y devuelva una 
cadena con los nombres de los números recibidos, separando cada número
con un guión medio. Por ejemplo, si el número recibido es 134,
 la función devolverá la cadena "uno - tres - cuatro"
'''
def numeros_a_cadena(numero):
    nombres = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }

    numero_str = str(numero)
    lista_numeros = list(numero_str)

    nombres_numeros = [nombres[num] for num in lista_numeros]

    cadena_resultado = ''
    for nombre in nombres_numeros:
        if cadena_resultado == '':
            cadena_resultado = nombre
        else:
            cadena_resultado = cadena_resultado + ' - ' + nombre

    return cadena_resultado

cadena_resultado = ""

while True:
    numeros = input("Ingrese un numero (o presione x para terminar): ")
    if numeros == "x":
        break
    else:
        lista_numeros = list(numeros)
        for numero in lista_numeros:
            cadena_resultado += numeros_a_cadena(numero) + " - "
        print(cadena_resultado[:-3])