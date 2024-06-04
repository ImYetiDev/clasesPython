"""Crea un diccionario contactos_avanzado donde las claves sean los nombres de las personas y los valores sean diccionarios con información detallada como teléfono, correo electrónico y dirección. 

a. Agrega al menos 3 contactos con su respectiva información detallada. 

b. Muestra al usuario la información detallada de un contacto específico. 

c.Permite al usuario actualizar la información de contacto de una persona existente."""

Contactos_avanzado = {"Marco": [123, "marquito@gmail.com", "cra 27 #23-45"], "Sofia": [1234, "sofi@gmail.com", "cra 23 #61-45"], "Carlos": [12345, "carlitos@gmail.com", "cra 45 #54-21"]}

usuarios = input("Informacion del empleado:  ")

if usuarios == "Marco":
    print (Contactos_avanzado["Marco"])
elif usuarios == "Sofia":
    print (Contactos_avanzado["Sofia"])
elif usuarios == "Carlos":
    print (Contactos_avanzado["Carlos"])
else:
    print ("No se encontro ningun contacto")


editar = input("Ingrese el nombre del contacto que desea actualizar: ")

if editar == "Marco":
    adicion = input("Ingrese los datos actualizados entre comillas: ")
    Contactos_avanzado["Marco"] = adicion
    print (Contactos_avanzado["Marco"])
elif editar == "Sofia":
    adicion = input("Ingrese los datos actualizados entre comillas: ")
    Contactos_avanzado["Sofia"] = adicion
    print (Contactos_avanzado["Sofia"])
elif editar == "Carlos":
    adicion = input("Ingrese los datos actualizados entre comillas: ")
    Contactos_avanzado["Carlos"] = adicion
    print (Contactos_avanzado["Carlos"])
else:
    print ("No se encontro ningun contacto")