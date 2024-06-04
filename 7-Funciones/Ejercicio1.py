'''
 Realiza una función que tome una lista de números enteros y
 devuelva dos listas ordenadas. La primera con los números pares y la
segunda con los números impares.

'''

def numeros (lista):
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    pares.sort()
    impares.sort()
    return pares, impares

numeros_enteros = [3,2,1,6,5,4,7,8,9,0]

pares,impares = numeros(numeros_enteros)
print("numeros pares",pares)
print("numeros impares",impares)
