""" Operadores Relacionales y lógicos:
Pide al usuario que ingrese tres números. Utiliza solo operadores lógicos y relacionales para
verificar si al menos dos de los números ingresados son iguales entre sí. Imprime un mensaje
indicando el resultado de la verificación, por ejemplo: "Al menos dos de los números son
iguales:" False """

n1 = int(input('Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))
n3 = int(input('Ingresa el tercer numero: '))

bool = n1 == n2 or n1 == n3 or n2 == n3
    
print(f'Al menos dos de los numeros son iguales: {bool}')