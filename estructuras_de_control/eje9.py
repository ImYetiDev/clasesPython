""" Pregunta al usuario que ingrese 6 números para jugar a la lotería. Luego, genera
aleatoriamente 6 números y determina cuántos números coinciden. Utiliza condicionales para
mostrar el premio correspondiente """

import random

user_numbers = []
lottery_numbers = []

for i in range(6):
  user_numbers.append(int(input(f'Ingrese el numero {i+1}: ')))

for i in range(6):
  lottery_numbers.append(random.randint(1, 5))

print(f'Los numeros de la loteria son: {lottery_numbers}')

coincidencias = 0

for i in user_numbers:
  if i in lottery_numbers:
    coincidencias += 1

if coincidencias == 6:
  print('Felicidades, has ganado el premio mayor')
elif coincidencias == 5:
  print('Felicidades, has ganado el segundo premio')
elif coincidencias == 4:
  print('Felicidades, has ganado el tercer premio')
elif coincidencias == 3:
  print('Felicidades, has ganado el cuarto premio')
else:
  print('Lo siento, no has ganado nada')

  