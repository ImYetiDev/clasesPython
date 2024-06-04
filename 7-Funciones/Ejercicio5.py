import math

def cantidad_pizzas(personas,tamaño ="grande"):

    if tamaño == "pequeña":
        capacidad = 6
    elif tamaño == "mediana":
        capacidad = 8
    else:
        capacidad = 10

    n_pizza = math.ceil(personas / capacidad)
    sobra = (n_pizza * capacidad) - personas
    no_repetir = capacidad - sobra

    print(f"para {personas} personas y una pizza {tamaño}, necesitas {n_pizza} pizzas")
    print(f"sobran {sobra} rebanadas de pizza y {no_repetir} personas NO alcanzan a repetir")

    return n_pizza,sobra,no_repetir 
cantidad_pizzas(int(input("ingrese el numero de personas: ")), input("ingrese el tamaño de la pizza: "))