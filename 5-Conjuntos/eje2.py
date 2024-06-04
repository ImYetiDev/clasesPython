Productos = {"Arroz", "Lentejas", "Huevos", "Pan"}

while True:
    usuario = input("que operacion desea realizar 1)Agregar producto, 2)Verificar disponibilidad del producto, 3)Eliminar producto, 4)Salir: ")
        
    if usuario == "1":
        producto_nuevo= input("agregue el producto nuevo ")
        Productos.add(producto_nuevo)
    elif usuario == "2":
        print(Productos)
    elif usuario == "3":   
        eliminar_producto = input("Ingrese el producto que desea eliminar")
        Productos.discard(eliminar_producto)
    else:
        break