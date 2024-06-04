""" Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha
calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres
calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del
examen final. 15% de la calificación de un trabajo final."""

calificacion1 = float(input("Ingrese la primera calificacion parcial: "))
calificacion2 = float(input("Ingrese la segunda calificacion parcial: "))
calificacion3 = float(input("Ingrese la tercera calificacion parcial: "))

promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3

examen_final = float(input("Ingrese la calificacion del examen final: "))

trabajo_final = float(input("Ingrese la calificacion del trabajo final: "))

calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print(f"La calificacion final del alumno es: {calificacion_final}")