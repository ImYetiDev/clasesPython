""" Solicita al usuario que ingrese un año y verifica si es bisiesto o no. Un año es bisiesto si es
divisible entre 4 pero no entre 100, o si es divisible entre 400. """

año = int(input("Ingresa un año: "))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
  print("El año es bisiesto")
else:
  print("El año no es bisiesto")