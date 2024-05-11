lista = []

while True:
    print("Aplicaciones con Listas")
    print("1. Ingresar lista nueva")
    print("2. Ordenar lista")
    print("3. Promedio lista")
    print("4. Buscar elemento")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        lista = []
        while True:
            entrada = input("Ingrese un número (ingrese un número negativo para terminar): ")
            if entrada < 0:
                break
            try:
                elemento = int(entrada)
                lista.append(elemento)
            except ValueError:
                print("Por favor, ingrese solo números enteros.")
            
    elif opcion == "2":
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            lista_ordenada = sorted(lista)
            print("Lista ordenada:", lista_ordenada)
            
    elif opcion == "3":
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            promedio = sum(lista) / len(lista)
            print("El promedio de la lista es:", promedio)
            
    elif opcion == "4":
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            entrada = input("Ingrese el número que desea buscar en la lista: ")
            try:
                elemento = int(entrada)
                cantidad = lista.count(elemento)
                if cantidad > 0:
                    print(f"El elemento {elemento} se encuentra en la lista y aparece {cantidad} veces.")
                else:
                    print("El elemento no se encuentra en la lista.")
            except ValueError:
                print("Por favor, ingrese solo números enteros.")
            
    elif opcion == "5":
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")