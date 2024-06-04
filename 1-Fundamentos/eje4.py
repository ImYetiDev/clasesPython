""" Operadores Relacionales y lógicos:
Pide al usuario que ingrese tres números. Utiliza solo operadores lógicos y relacionales para
verificar si al menos dos de los números ingresados son iguales entre sí. Imprime un mensaje
indicando el resultado de la verificación, por ejemplo: "Al menos dos de los números son
iguales:" False """

n1 = int (input("ingrese primer numero: ") )
n2 = int (input("ingrese segundo numero: ") )
n3 = int (input("ingrese tercer numero: ") )

if n1 == n2 or n1 == n3 or n2 == n3:
    print("Al menos dos de los numeros son iguales: True")
else:
    print("Al menos dos de los numeros son iguales: False")