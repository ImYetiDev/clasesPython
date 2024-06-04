'''
Finaliza el siguiente código con una gestión completa de sus excepciones. El objetivo del
programa es solicitar al usuario una posición de una lista y devolver el valor que se encuentra
en dicha posición. Prueba el programa enviando una posición inexistente y enviando una letra
como posición. El programa sólo terminará cuando se ejecute correctamente

'''
lista = [3, 5, 6, 8]
while True:
    try:
        pos = int(input("Ingrese la posicion del elemento que desea obtener: "))
        print(f"El valor en la posicion {pos} es {lista[pos]}")
        break
    except IndexError:
        print("Error: La posicion ingresada esta fuera del rango de la lista.")
    except ValueError:
        print("Error: Por favor, ingrese una posicion válida (numero entero).")
    except Exception as e:
        print("Error desconocido:", e)
