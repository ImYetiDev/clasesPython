""" Imagina que estás diseñando un programa para un sistema de facturación donde necesitan
redondear los montos de las transacciones financieras al valor entero mayor más próximo al
valor entregado.
Debera solicitarle al usuario el monto de 5 transacciones todas con valores reales, además
calcular el valor total de lo que se perdio en el redondeo en todas las transacciones y
presentar este valor con un redondeo de hasta 3 decimales. Debes mostrar cada monto
original y el valor redondeado, la suma de todas las transacciones redondeadas y el valor que
se perdio del redondeo. """
import math

transaccion1 = float(input("Ingrese el monto de la primera transaccion: "))
transaccion2 = float(input("Ingrese el monto de la segunda transaccion: "))
transaccion3 = float(input("Ingrese el monto de la tercera transaccion: "))
transaccion4 = float(input("Ingrese el monto de la cuarta transaccion: "))
transaccion5 = float(input("Ingrese el monto de la quinta transaccion: "))

transaccion1_redondeada = math.ceil(transaccion1)
transaccion2_redondeada = math.ceil(transaccion2)
transaccion3_redondeada = math.ceil(transaccion3)
transaccion4_redondeada = math.ceil(transaccion4)
transaccion5_redondeada = math.ceil(transaccion5)

diferencia1 = transaccion1 + transaccion1_redondeada
diferencia2 = transaccion2 + transaccion2_redondeada
diferencia3 = transaccion3 + transaccion3_redondeada
diferencia4 = transaccion4 + transaccion4_redondeada
diferencia5 = transaccion5 + transaccion5_redondeada

print(f'Valor original 1 {transaccion1} y el redondeado {transaccion1_redondeada}')
print(f'Valor original 2 {transaccion2} y el redondeo {transaccion2_redondeada}')
print(f'Valor original 3 {transaccion3} y el redondeo {transaccion3_redondeada}')
print(f'Valor original 4 {transaccion4} y el redondeo {transaccion4_redondeada}')
print(f'Valor original 5 {transaccion5} y el redondeo {transaccion5_redondeada}')

diferencia = diferencia1 + diferencia2 + diferencia3 + diferencia4 + diferencia5

print(f'El valor de perdidas redondeando {diferencia}')