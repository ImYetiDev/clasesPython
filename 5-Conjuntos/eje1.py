emails = {"medinaylang@gmail.com", "anyjeff04@hotmail.com", "ylangvaleria@gmail.com", "angel.ylang@gmail.com"}

while True:
    usuario = input("que operacion desea realizar 1)Agregar cliente, 2)Verificar cliente, 3)Eliminar cliente, 4)Salir: ")
        
    if usuario == "1":
        cliente_nuevo= input("agregue el nuevo cliente")
        emails.add(cliente_nuevo)
    elif usuario == "2":
        print(emails)
    elif usuario == "3":   
        eliminar_cliente = input("Ingrese el cliente que desea eliminar")
        emails.discard(eliminar_cliente)
    else:
        break