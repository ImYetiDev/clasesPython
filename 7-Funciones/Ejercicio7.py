'''
Construir una función recursiva que lleve la cuenta de las veces que un aspirante intentó ingresar al SENA hasta que lo logra. La función
tendrá definido en el código el puntaje mínimo para aprobar el examen de ingreso (70 puntos) y deberá recibir como argumento el puntaje
que el aspirante sacó (valor aleatorio), mientras el aspirante no apruebe el examen, la función se invocará así misma hasta cuando por fin
lo apruebe la función se detendrá y mostrará el número de intentos realizados por el aspirante.
'''

import random

def intentos_ingreso_SENA(puntaje_obtenido, puntaje_minimo=70, intentos=1):
    if puntaje_obtenido >= puntaje_minimo:
        print(f"El aspirante aprobo el examen en {intentos} intentos.")
    else:
        puntaje_obtenido = random.randint(40, 100)
        print(f"Intento {intentos}: El aspirante obtuvo {puntaje_obtenido} puntos.")
        intentos += 1
        intentos_ingreso_SENA(puntaje_obtenido, puntaje_minimo, intentos)

puntaje_inicial = random.randint(40, 100)
print(f"Puntaje inicial del aspirante: {puntaje_inicial}")
intentos_ingreso_SENA(puntaje_inicial)
