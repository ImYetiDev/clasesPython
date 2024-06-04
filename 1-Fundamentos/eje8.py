calparcial1 = int (input("ingrese su primera calificacion parcial: "))
calparcial2 = int (input("ingrese su segunda calificacion parcial: "))
calparcial3 = int (input("ingrese su tercera calificacion parcial: "))
examenFinal = int (input("ingrese la calificacion de su examen final: "))
trabajoFinal = int (input("ingrese la calificacion de su trabajo final: "))

promedio = ((calparcial1 + calparcial2 + calparcial3)/3)

nota_final = ((promedio * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15))

print ("Su primera calificacion parcial es: ", calparcial1)
print ("Su segunda calificacion parcial es: ", calparcial2)
print ("Su tercera calificacion parcial es: ", calparcial3)

print ("Su nota final es:", nota_final)