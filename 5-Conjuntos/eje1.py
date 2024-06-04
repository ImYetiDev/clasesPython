""" Desarrolla un programa para gestionar clientes de una empresa. Utiliza un conjunto para
almacenar los correos electrónicos de los clientes registrados.
Permite al usuario agregar nuevos clientes,
verificar si un cliente ya está registrado y
eliminar clientes """

clientes_registrados = {'David@gmail.com', 'Juan@gmail.com', 'Ana@gmail.com', 'Luis@gmail.com', 'Maria@gmail.com', 'Pedro@gmail.com', 'Sofia@gmail.com', 'Carlos@gmail.com', 'Laura@gmail.com', 'Miguel@gmail.com'}

def agregar_cliente(cliente):
    clientes_registrados.add(cliente)
    print(f'Cliente {cliente} agregado con éxito')

def verificar_cliente(cliente):
    if cliente in clientes_registrados:
        print(f'El cliente {cliente} ya está registrado')
    else:
        print(f'El cliente {cliente} no está registrado')

def eliminar_cliente(cliente):
    if cliente in clientes_registrados:
        clientes_registrados.remove(cliente)
        print(f'Cliente {cliente} eliminado con éxito')
    else:
        print(f'El cliente {cliente} no está registrado')

def main():
    while True:
        print('\n1. Agregar cliente')
        print('2. Verificar cliente')
        print('3. Eliminar cliente')
        print('4. Salir\n')
        opcion = int(input('Opción: '))

        if opcion == 1:
            cliente = input('Ingrese el correo del cliente: ')
            agregar_cliente(cliente)
        elif opcion == 2:
            cliente = input('Ingrese el correo del cliente: ')
            verificar_cliente(cliente)
        elif opcion == 3:
            cliente = input('Ingrese el correo del cliente: ')
            eliminar_cliente(cliente)
        elif opcion == 4:
            print('Saliendo, Adios...')
            break
        else:
            print('Opción inválida')

main()