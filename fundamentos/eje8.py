""" Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha
calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres
calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del
examen final. 15% de la calificación de un trabajo final.
"""

calificacion1 = int(input('Ingresa la calificacion 1: '))
calificacion2 = int(input('Ingresa la calificacion 2: '))
calificacion3 = int(input('Ingresa la calificacion 3: '))
examen_final = int(input('Ingresa la calificacion del examen final: '))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3
trabajo_final = int(input('Ingresa la calificacion del trabajo final: '))
calificacion_final = (promedio * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print(f'La calificacion final es: {calificacion_final}')