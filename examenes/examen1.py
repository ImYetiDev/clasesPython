""" El programa solicita al usuario dos numeros y una operacion matematica( suma, resta, multiplicacion, division). Luego, realiza la operacion seleccionada y muestra el resultado.
Se repite el proceso hasta que el usuario decida """
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

console = True
while console:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    operation = int(input("\n\nIngrese la operacion que desea realizar: "))
    if operation == 1:
        print("La suma de los numeros es: ", n1 + n2)
    elif operation == 2:
        print("La resta de los numeros es: ", n1 - n2)
    elif operation == 3:
        print("La multiplicacion de los numeros es: ", n1 * n2)
    elif operation == 4:
        if n2 == 0:
            print('No se puede dividir por 0')
        else:
            print("La division de los numeros es: ", n1 / n2)
    elif operation == 5:
        console = False
    else:
        print("Operacion invalida")                                                                                                           