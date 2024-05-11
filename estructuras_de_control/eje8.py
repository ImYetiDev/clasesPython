""" Solicita al usuario que ingrese una contraseña y verifica si cumple con ciertos criterios, como
tener al menos 8 caracteres
incluir letras mayúsculas
minúsculas 
números """

password = input("Ingresa una contraseña: ")

if len(password) >= 8:
  if any(char.isupper() for char in password):
    if any(char.islower() for char in password):
      if any(char.isdigit() for char in password):
        print("Contraseña valida")
      else:
        print("La contraseña debe contener al menos un numero")
    else:
      print("La contraseña debe contener al menos una letra minuscula")
  else:
    print("La contraseña debe contener al menos una letra mayuscula")
else:
  print("La contraseña debe tener al menos 8 caracteres")