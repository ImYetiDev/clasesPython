import random

# Lista de adjetivos positivos
adj_positivos = [
    "creativo",
    "amable",
    "diligente",
    "generoso",
    "empático",
    "valiente",
    "inteligente",
    "apasionado",
    "comprensivo",
    "leal"
]

# Lista de frases sobre el destino
frases_destino = [
    "grandes aventuras te esperan a la vuelta de la esquina.",
    "encontrarás lo que buscas en el lugar menos esperado.",
    "la oportunidad de tu vida está a punto de llegar.",
    "se acerca un cambio significativo para mejor.",
    "tu esfuerzo pronto será recompensado."
]

def generar_mensaje_animo(nombre=""):
    if nombre:
        saludo = f"Hola, {nombre}!"
    else:
        saludo = "Hola!"

    # Seleccionar un adjetivo y una frase del destino de manera aleatoria
    adjetivo = random.choice(adj_positivos)
    frase = random.choice(frases_destino)

    # Crear el mensaje final
    mensaje = f"{saludo} Eres una persona {adjetivo} y {frase}"
    return mensaje

# Prueba de la función
nombre_usuario = input("Ingresa tu nombre (puedes dejarlo en blanco y presionar enter): ")
print(generar_mensaje_animo(nombre_usuario))
