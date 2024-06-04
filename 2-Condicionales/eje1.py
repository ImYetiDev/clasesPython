"""En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la
temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente.
Escribir un programa que controle el estado del motor y lo apague si la temperatura supera
los 80 grados."""

temperatura = int (input("Ingresa la temperatura del motor: "))

if temperatura < 80:
    print ("El motor sigue encendido.")
else:
    print ("El motor se debe apagar.")
