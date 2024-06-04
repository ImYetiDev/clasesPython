import random

frutas = ["manzana", "banana", "naranja", "uva", "pera", "sandía", "cereza", "durazno", "kiwi", "mango"]
fruta_secret = random.choice(frutas)

intentos_max = 5

intentos_realizados = 0

while intentos_realizados < intentos_max:
    respuesta = input("Adivine la fruta: ")
    intentos_realizados+=1
    if respuesta == fruta_secret:
        print("¡Correcto! La fruta es: ", fruta_secret)
        break
    else:
        if intentos_realizados == 1:
            print("Incorrecto. Pista: La fruta tiene ")
            print("la longitud de la palabra es: ", len(fruta_secret))
            print("La primera y ultima letra de la fruta son: ", fruta_secret[0], fruta_secret[-1])
        elif intentos_realizados == 2:
            print("Incorrecto. Pista: La fruta tiene ")
            print("la longitud de la palabra es: ", len(fruta_secret))
            print("La primera y ultima letra de la fruta son: ", fruta_secret[0], fruta_secret[-1])
        elif intentos_realizados == 3:
            print("Todavía no correcto. Pista: La fruta tiene ")
            print("la longitud de la palabra es: ", len(fruta_secret))
            print("La primera y ultima letra de la fruta son: ", fruta_secret[0], fruta_secret[-1])
        else:
            print("Incorrecto. La fruta era: ", fruta_secret)
            break