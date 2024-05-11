""" Crear tres lista con la siguiente información (nombre, edad, sexo),
imprimir cual es la persona más joven y
cual es la persona de más edad contar cuantas son hombres y cuantas son mujeres """

list1 = ["David", 20 , "M"]
list2 = ["Maria", 30 , "F"]
list3 = ["Juan", 25 , "M"]

listas = [list1, list2, list3]

edades = []
sexos = []
for lista in listas:
    edades.append(lista[1])
    sexos.append(lista[2])

print("La persona más joven es: ", listas[edades.index(min(edades))][0])
print({edades.index(min(edades))})
print("La persona de más edad es: ", listas[edades.index(max(edades))][0])

print("Cantidad de hombres: ", sexos.count("M"))
print("Cantidad de mujeres: ", sexos.count("F"))