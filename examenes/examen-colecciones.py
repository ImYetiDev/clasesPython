"""Elabore un programa para gestionar una lista de compras. Debe tener un menu con las siguientes opciones:

***GESTION LISTA DE COMPRAS****
    1. Agregar productos
    2. Eliminar productos
    3. Mostrar la lista de compras 
    4. Salir
Los usuarios pueden agregar productos a la lista indicando su nombre, cantidad, precio por unidad

productos = { 'Manzanas': {'cantidad': 5, 'precio': 1.5}, 'Leche': {'cantidad': 2, 'precio': 2.0}, 'Pan': {'cantidad': 1, 'precio': 0.75} }

Tambien debe permitir eliminar productos si es necesario, y mostrar la lista de compras actualizada con los producto cantidad, precio, valor total del producto y el valor total de la lista."""

productos = { }


compras = input("Actualice su lista de compreas, si desea agregar un producto marque 1), si desea eliminar producto marque 2), si desea mostrar la lista de compreas marque 3), si desea salir marque 4).")


if compras == "1":
    Aproducto = input("Ingrese un nuevo producto: ")
    cant = input("Ingrese la cantidad: ")
    precio = input("Ingrese el precio: ")
    productos[Aproducto] = productos["Cantidad"] = cant 
    productos[Aproducto] = productos["Precio"] = precio
elif compras == "2":
    Eproducto = input("Ingrese el producto que va a eliminar: ")
    print (productos.pop(Eproducto))
    print (productos)

elif compras == "3":
    print (productos)

elif compras == "4":
    print ("Good Bye")

