""" Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es
correcto. Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. El programa
debe terminar automáticamente al quinto intento fallido """


contraseñaIngreso = input("Crea la contraseña: ")

intentos = 0
contraseñaIntento = ""

while contraseñaIngreso != contraseñaIntento and intentos < 6:
    contraseñaIntento = input("Ingrese su contraseña: ")
    
    if contraseñaIngreso == contraseñaIntento:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
        intentos += 1
        if intentos == 5:
            print("Intentos agotados")
            break