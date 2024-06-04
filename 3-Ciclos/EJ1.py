""" Elabore un algoritmo para que los niños practiquen las tablas de multiplicar.
El programa debe
solicitar al niño que tabla quiere repasar y luego hacerle 6 preguntas aleatorias de esa tabla.
Si el niño responde correctamente, se le felicitará y animará. Si responde incorrectamente, se
le indicará su error. Al finalizar las 6 preguntas, se le dirá cuántas respondió correctamente. Si
acierta al menos 3 preguntas, se le sugiere que siga practicando esa tabla y se le muestra la
tabla completa. Si responde correctamente a todas las preguntas, se le indicará que se sabe
la tabla y se le invitara a que siga repasando otras tablas de multiplicar. Si responde
incorrectamente a menos de 3 preguntas, se le mostrará la tabla completa y se le preguntará
si quiere volver a estudiarla o salir.
 """
import random
print("Bienvenido al programa de práctica de tablas de multiplicar")
 
tabla = int(input("Ingrese la tabla que desea repasar: "))

preguntas_correctas = 0

for i in range(6):
    num1 = tabla
    num2 = random.randint(1, 10)
    
    respuesta = int(input(f"{num1} x {num2} = "))
    
    if respuesta == num1 * num2:
        print("¡Correcto! Muy bien.")
        preguntas_correctas += 1
    else:
        print("Incorrecto. La respuesta correcta es:", num1 * num2)
        
print("Las preguntas han terminado. Respondiste correctamente", preguntas_correctas, "preguntas.")

if preguntas_correctas == 6:
    print("¡Felicidades! Te sabes la tabla de multiplicar del", tabla)
    print("Sigue repasando otras tablas.")
    
elif preguntas_correctas >= 3:
    print("Sigue practicando la tabla del", tabla)
    print("Aquí tienes la tabla completa:")
    for i in range(1, 11):
        print(tabla, "x", i, "=", tabla * i)
    
    
    
        
        