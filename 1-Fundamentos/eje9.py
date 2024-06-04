transaccion1 = float (input("Ingresa el valor de la 1 transaccion: "))
transaccion2 = float (input("Ingresa el valor de la 2 transaccion: "))
transaccion3 = float (input("Ingresa el valor de la 3 transaccion: "))
transaccion4 = float (input("Ingresa el valor de la 4 transaccion: "))
transaccion5 = float (input("Ingresa el valor de la 5 transaccion: "))

redondeo1 =round(transaccion1)
redondeo2 =round(transaccion2)
redondeo3 =round(transaccion3)
redondeo4 =round(transaccion4)
redondeo5 =round(transaccion5)

sum = (redondeo1 + redondeo2 + redondeo3 + redondeo4 + redondeo5)
perdidas = (transaccion1 - redondeo1) + (transaccion2 - redondeo2) + (transaccion3 - redondeo3) + (transaccion4 - redondeo4) +(transaccion5 - redondeo5)

print(f"Monto Original: {transaccion1}  , Monto Redondeado: {redondeo1}" )
print(f"Monto Original: {transaccion2}  , Monto Redondeado: {redondeo2}" )
print(f"Monto Original: {transaccion3}  , Monto Redondeado: {redondeo3}" )
print(f"Monto Original: {transaccion4}  , Monto Redondeado: {redondeo4}" )
print(f"Monto Original: {transaccion5}  , Monto Redondeado: {redondeo5}" )

print(f"La suma de todas las transacciones es: {sum} ")
print(f"la perdida por redonde es: {perdidas}")