"""
Se requiere una funcion que simule tirar los dado, deberá solicitar cuantas personas van a jugar, en cada turno se pedirá el nombre de lapersona y la aplicación lanzará los dados, debe indicar cuanto saqué con cada dado y la suma de los dos, deberá guardar el nombre de la
persona y el valor de la suma de los dos dados, al fi nal deberá indicar qué jugador tuvo el mayor valor y ganó el juego.
"""
import random

def tirar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def jugar():
    num_jugadores = int(input("Cuantas personas van a jugar? "))
    jugadores = {}
    
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores[nombre] = 0
        
    for jugador in jugadores:
        input(f"Turno de {jugador}. Presione Enter para lanzar los dados.")
        dado1, dado2 = tirar_dados()
        suma_dados = dado1 + dado2
        jugadores[jugador] = suma_dados
        print(f"{jugador} lanzo los dados y saco: {dado1} y {dado2}. Suma total: {suma_dados}")
    
    max_puntuacion = max(jugadores.values())
    ganadores = [jugador for jugador, puntuacion in jugadores.items() if puntuacion == max_puntuacion]
    
    if len(ganadores) == 1:
        print(f"El ganador es: {ganadores[0]} con una puntuacion de {max_puntuacion}")
    else:
        print("Hubo un empate")
        print("Los ganadores son:")
        for ganador in ganadores:
            print(f"{ganador} con una puntuacion de {max_puntuacion}")

jugar()
