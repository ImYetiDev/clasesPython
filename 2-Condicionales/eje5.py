
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))


if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("No es un triángulo válido.")
elif lado1 == lado2 == lado3:
    print("Es un triángulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")
