""" Crea un sistema para controlar el inventario de productos de una tienda. Utiliza un conjunto para
almacenar los códigos de barras de los productos disponibles. Permite al usuario agregar
nuevos productos al inventario, verificar la disponibilidad de un producto y eliminar productos
obsoletos. """

productos_disponibles = {123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234, 123456}

def agregar_producto(producto):
    productos_disponibles.add(producto)
    print(f'Cliente {producto} agregado con éxito')

def verificar_cliente(producto):
    if producto in productos_disponibles:
        print(f'El cliente {producto} ya está registrado')
    else:
        print(f'El cliente {producto} no está registrado')

def eliminar_cliente(producto):
    if producto in productos_disponibles:
        productos_disponibles.remove(producto)
        print(f'Cliente {producto} eliminado con éxito')
    else:
        print(f'El producto {producto} no está registrado')

def main():
    while True:
        print('\n1. Agregar producto')
        print('2. Verificar producto')
        print('3. Eliminar producto')
        print('4. Salir\n')
        opcion = int(input('Opción: '))

        if opcion == 1:
            producto = int(input('Ingrese el código de barras del producto: '))
            agregar_producto(producto)
        elif opcion == 2:
            producto = int(input('Ingrese el código de barras del producto: '))
            verificar_cliente(producto)
        elif opcion == 3:
            producto = int(input('Ingrese el código de barras del producto: '))
            eliminar_cliente(producto)
        elif opcion == 4:
            print('Saliendo, Adios...')
            break
        else:
            print('Opción inválida')

main()