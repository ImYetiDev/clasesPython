""" Realiza una función llamada agregar_una_vez(lista, elemento) que reciba una lista y unelemento. La función debe añadir el elemento al fi nal de la lista con la condición de no repetirningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar unerror de tipo ValueError que debes capturar y mostrar este mensaje en su lugar: """

element = int(input('Ingrese un numero:'))

def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}")
        else:
            lista.append(elemento)
    except ValueError as error:
        print(error)
print('Gracias por usar este programa')

lista=[2,4,6,8,10]
mi_lista = [1, 2, 3, 4, 5]
agregar_una_vez(mi_lista,element)