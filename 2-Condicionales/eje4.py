""" Solicita al usuario que ingrese el peso de un paquete y el destino del envío. Utiliza estructuras
condicionales para calcular el costo de envío según el peso y el destino. Considera las
siguientes tarifas para destinos nacionales e internacionales.

Peso en KG  |  Nacional  |  Internacional
0 a 3       |  29.340    |  46.380
4 a 7       |  55.740    |  100.380
8 a 10      |  75.540    |  132.780
11 a 15     | 108.540    |  186.780
16 a 20     | 141.540    |  240.780
Por kg extra|   6.840    |  12.000 

Saber si el destino es nacional o internacional X
Saber el peso del paquete                       X
Calcular el costo de envío
Imprimir el costo de envío """

destino = int(input("Ingresa 0 para envio nacional y 1 para envio internacional: "))

""" Comparacion de entrada valor correcto """
if destino == 1 or destino == 0:
  peso = int(input('Ingresa el peso en KG: '))

  """ Linea 1 de precios de la tabla """
  if peso >= 0 and peso < 4:
    if destino == 0:
      costo = 29_340
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 46_380
      print(f'El precio por envio seria: {costo}')
  
  """ Linea 2 de precios de la tabla """
  if peso > 3 and peso < 8:
    if destino == 0:
      costo = 55_740 
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 100_380
      print(f'El precio por envio seria: {costo}')

  """ Linea 3 de precios de la tabla """
  if peso > 7 and peso < 11:
    if destino == 0:
      costo = 75_540
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 132_780
      print(f'El precio por envio seria: {costo}')

  """ Linea 4 de precios de la tabla """
  if peso > 10 and peso < 16:
    if destino == 0:
      costo = 108_540
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 186_780
      print(f'El precio por envio seria: {costo}')

  """ Linea 5 de precios de la tabla """ 
  if peso > 15 and peso < 21:
    if destino == 0:
      costo = 141_540
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 240_780
      print(f'El precio por envio seria: {costo}')

  """ Linea 6 de precios de la tabla """
  if peso > 20:
    if destino == 0:
      costo = 141_540 + (peso - 20) * 6_840
      print(f'El precio por envio seria: {costo}')
    elif destino == 1:
      costo = 240_780 + (peso - 20) * 12_000
      print(f'El precio por envio seria: {costo}')








else:
  print('El valor ingresado no es valido')