""" Pide al usuario que ingrese las longitudes de los lados de un triángulo. Utiliza condicionales
para determinar si el triángulo es equilátero, isósceles, escaleno o no válido. """

lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
  print("Tu triangulo no es valido")
else:
  if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")
  elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triangulo es isosceles")
  elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("El triangulo es escaleno")