"""En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para
determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe
marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares
de calidad, se debe marcar como aprobada y continuar con la producción.
Realice un programa que lea una entrada binaria en la que los 1s significan estándares de
calidad cumplidos y los 0s significan estándares de calidad No cumplidos. El programa debe
rechazar la pieza ante cualquier estándar no cumplido. """

productos = ['audifonos', 'pc', 'laptop', 'mouse', 'teclado', 'disco duro']
productos_aprobados = []
productos_rechazados = []


print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[0]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[0])
    elif parametro == 0:
        productos_rechazados.append(productos[0])
else:
        print('No elegiste un parametro valido')

print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[1]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[1])
    elif parametro == 0:
        productos_rechazados.append(productos[1])
else:
        print('No elegiste un parametro valido')
        
print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[2]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[2])
    elif parametro == 0:
        productos_rechazados.append(productos[2])
else:
        print('No elegiste un parametro valido')
        
print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[3]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[3])
    elif parametro == 0:
        productos_rechazados.append(productos[3])
else:
        print('No elegiste un parametro valido')
        
print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[4]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[4])
    elif parametro == 0:
        productos_rechazados.append(productos[4])
else:
        print('No elegiste un parametro valido')
        
print('Califica 1 para aprobado y 0 para desaprobado')
parametro = int(input(f"{productos[5]} "))
if parametro == 1 or parametro == 0:
    if parametro == 1:
        productos_aprobados.append(productos[5])
    elif parametro == 0:
        productos_rechazados.append(productos[5])
else:
        print('No elegiste un parametro valido')
        
print(f'Los productos aprobados son: {productos_aprobados}')
print(f'Los productos desaprobados son: {productos_rechazados}')