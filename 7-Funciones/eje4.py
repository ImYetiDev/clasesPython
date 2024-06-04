"""¡Madame Adivinadona te ha contratado para que le realices una aplicación en donde la persona ingresa su nombre y le va a decir cómo es y qué le depara el destino. Debes crear dos listas: una con adjetivos positivos y otra con frases que expresen lo que le depara el destino. Luego, debes usar estas listas en la función generar_mensaje_animo. Si la persona no ingresa el nombre debera iniciar con un 'Hola'"""

import random

positivos = ["Increible", "Fascinante", "Interesante", "Emocionante"]
frases = ["Ganarás la loteria", "Tendras una linda Familia", "Encontraras a tu verdadero amor", "Seras Millonario"]

def generar_mensaje_animo(nombre=""):
    if nombre:
        saludo = f"Hola, {nombre}!"
    else:
        saludo = "Hola!"

    adjetivo = random.choice(positivos)
    frase = random.choice(frases)

    mensaje = f"{saludo} Eres una persona {adjetivo} y {frase}"
    return mensaje

nombre_usuario = input("Ingresa tu nombre (puedes dejarlo en blanco y presionar enter): ")
print(generar_mensaje_animo(nombre_usuario))