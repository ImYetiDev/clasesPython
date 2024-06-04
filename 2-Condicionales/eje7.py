""" Genera dos números aleatorios y muestra al usuario la suma de los números. Pídele al
usuario que adivine cuáles fueron los números originales. Utiliza condicionales para
determinar si la respuesta del usuario es correcta. """
import random

num1 = random.randint(1, 5)
num2 = random.randint(1, 5)

suma = num1 + num2 

print(f'La suma es: {suma}')

print('Cuales crees que son los numeros usados en la suma [1-5]')

input1 = int(input('Ingrese el primer numero: '))
input2 = int(input('Ingrese el segundo numero: '))

if input1 == num1 and input2 == num2:
  print('Felicidades, has acertado los 2 numeros')
elif input1 == num1:
  print(f'Lo siento, solo encontraste uno, eran {num1} y {num2}')
elif input2 == num2:
  print(f'Lo siento, solo encontraste uno, eran {num1} y {num2}')
else:
  print(f'Lo siento, los numeros eran {num1} y {num2}')