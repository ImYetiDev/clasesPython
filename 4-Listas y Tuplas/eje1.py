num_elementos = int(input("Ingrese el número de elementos que desea en la lista: "))


lista = []


for i in range(num_elementos):
    elemento = input("Ingrese el elemento {}: ".format(i+1))
    lista.append(elemento)

print("Lista original:", lista)

print("Lista invertida:", lista[::-1])