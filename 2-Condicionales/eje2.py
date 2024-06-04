estrato = int (input("Ingrese su estrato: "))
edad = int (input("Ingrese su edad: "))
descuento = int
matricula = int (input("ingrese el valor de la Maricula: "))

if estrato == 1 and edad < 18:
    descuento = (matricula -(matricula * 0.20))
elif estrato == 1 and edad >= 18:
    descuento = (matricula -(matricula * 0.15))
elif estrato == 2 and edad < 18:
    descuento = (matricula -(matricula * 0.10))
elif estrato == 2 and edad >= 18:
    descuento = (matricula -(matricula * 0.05))
else:
    print ("No obtiene descuento.")

print (f"El valor de su matricula es: {matricula} pero con el descuento es: {descuento}")