#Crea un diccionario llamado empleados donde las claves sean los números de identificación y los valores sean diccionarios con el nombre y el cargo del empleado. Agrega al menos 5 empleados con su respectiva información. Permite al usuario buscar empleados por su número de identificación y mostrar toda su información. Permite al usuario eliminar un empleado por su número de identificación.

empleados = {"1":["Marco", "Gerente"], "2":["Maria", "Secretaria"], "3": ["Sofia" , "Contadora"], "4": ["Carlos" , "Chef"], "5": ["Santiago" , "Administrador"]}

usuarios = input("Buscar empleados por su numero ID: ")

if usuarios == "1":
    print (empleados["1"])
elif usuarios == "2":
    print (empleados["2"])
elif usuarios == "3":
    print (empleados["3"])
elif usuarios == "4":
    print (empleados["4"])
elif usuarios == "5":
    print (empleados["5"])
else:
    print ("No se encontro un usuario con este ID")

eliminar_emp = input("Ingrese el ID del empleado que desee eliminar: ")

if eliminar_emp == "1":
    del(empleados["1"])
elif eliminar_emp == "2":
    del(empleados["2"])
elif eliminar_emp == "3":
    del(empleados["3"])
elif eliminar_emp == "4":
    del(empleados["4"])
elif eliminar_emp == "5":
    del(empleados["5"])


mensaje = input("Desea verificar la lista de empleados? conteste Y para si y N para no: ")
if mensaje == "Y":
    print(empleados)
else:
    print("Hasta Luego")



