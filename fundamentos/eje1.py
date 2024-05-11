""" Solicita al usuario que ingrese su nombre y su edad, luego imprime un mensaje personalizado
utilizando f-strings para saludarlo y decirle cuántos años tiene. """


name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hola {}'.format(name))
print('Tu edad es {}'.format(age))