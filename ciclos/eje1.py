""" Elabore un algoritmo para que los niños practiquen las tablas de multiplicar. 
El programa debe solicitar al niño que tabla quiere repasar
y luego hacerle 6 preguntas aleatorias de esa tabla.

Si el niño responde correctamente, se le felicitará y animará.
Si responde incorrectamente, se le indicará su error.

Al finalizar las 6 preguntas, se le dirá cuántas respondió correctamente.
Si acierta al menos 3 preguntas, se le sugiere que siga practicando esa tabla y se le muestra la
tabla completa.

Si responde correctamente a todas las preguntas, se le indicará que se sabe
la tabla y se le invitara a que siga repasando otras tablas de multiplicar.

Si responde incorrectamente a menos de 3 preguntas, se le mostrará la tabla completa y se le preguntará
si quiere volver a estudiarla o salir """
import random

tabla = int(input('Ingrese la tabla que desea repasar: '))

correctas = 0

for i in range(6):
  num = random.randint(1, 10)
  print(f'{tabla} x {num} = ')
  respuesta = int(input('Ingrese la respuesta: '))

  if respuesta == tabla * num:
    print('Correcto')
    correctas += 1
  else:
    print('Incorrecto')

if correctas >= 3:
  print('Sigue practicando la tabla')
  for i in range(1, 11):
    print(f'{tabla} x {i} = {tabla * i}')

if correctas == 6:
  print('Ya te sabes la tabla')
  print('Sigue repasando otras tablas de multiplicar')

if correctas < 3:
  print('Estudia la tabla completa')
  for i in range(1, 11):
    print(f'{tabla} x {i} = {tabla * i}')
  respuesta = input('¿Quieres volver a estudiarla? (s/n): ')
  if respuesta == 's':
    for i in range(6):
      num = random.randint(1, 10)
      print(f'{tabla} x {num} = ')
      respuesta = int(input('Ingrese la respuesta: '))

      if respuesta == tabla * num:
        print('Correcto')
        correctas += 1
      else:
        print('Incorrecto')
    if correctas >= 3:
      print('Sigue practicando la tabla')
      for i in range(1, 11):
        print(f'{tabla} x {i} = {tabla * i}')
    if correctas == 6:
      print('Ya te sabes la tabla')
      print('Sigue repasando otras tablas de multiplicar')
  else:
    print('Adios')