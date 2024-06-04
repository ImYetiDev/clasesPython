
Con = input("Ingrese una contraseña: ")

longitud_suf = len(Con) >= 8
contiene_may = any(c.isupper() for c in Con)
contiene_min = any(c.islower() for c in Con)
contiene_numeros = any(c.isdigit() for c in Con)

if longitud_suf and contiene_may and contiene_min and contiene_numeros:
    print("La contraseña cumple con todos los criterios.")
else:
    print("La contraseña no cumple con todos los criterios.")
