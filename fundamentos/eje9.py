""" Imagina que estás diseñando un programa para un sistema de facturación donde necesitan
redondear los montos de las transacciones financieras al valor entero mayor más próximo al
valor entregado.
Debera solicitarle al usuario el monto de 5 transacciones todas con valores reales, además
calcular el valor total de lo que se perdio en el redondeo en todas las transacciones y
presentar este valor con un redondeo de hasta 3 decimales. Debes mostrar cada monto
original y el valor redondeado, la suma de todas las transacciones redondeadas y el valor que
se perdio del redondeo.
 """
 
monto1 = float(input('Ingresa el monto: '))
monto2 = float(input('Ingresa el monto: '))
monto3 = float(input('Ingresa el monto: '))
monto4 = float(input('Ingresa el monto: '))
monto5 = float(input('Ingresa el monto: '))

redondeo1 = round(monto1)
redondeo2 = round(monto2)
redondeo3 = round(monto3)
redondeo4 = round(monto4)
redondeo5 = round(monto5)

perdida = (monto1 - redondeo1) + (monto2 - redondeo2) + (monto3 - redondeo3) + (monto4 - redondeo4) + (monto5 - redondeo5)

print(f'Monto original: {monto1} Redondeo: {redondeo1}\n')
print(f'Monto original: {monto2} Redondeo: {redondeo2}\n')
print(f'Monto original: {monto3} Redondeo: {redondeo3}\n')
print(f'Monto original: {monto4} Redondeo: {redondeo4}\n')
print(f'Monto original: {monto5} Redondeo: {redondeo5}\n')

print(f'Perdida por redondeo: {perdida}')