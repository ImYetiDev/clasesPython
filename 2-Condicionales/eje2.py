"""Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad.
Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la
matrícula.
Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.
Si el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la
edad es 18 años o mas, el descuento será del 5%.
Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento. """

edad = int(input("Ingrese la edad del estudiante: "))
estrato = int(input("Ingrese el estrato del estudiante: "))
valor_matricula = float(input("Ingrese el valor de la matrícula: "))

descuento = 0

if estrato == 1:
    if edad < 18:
        descuento = valor_matricula * 0.20
        print(f"El valor de la matrícula es {valor_matricula} y el descuento es {descuento}.")
        print(f"El valor a pagar es {valor_matricula - descuento}.")
    else:
        descuento = valor_matricula * 0.15
        print(f"El valor de la matrícula es {valor_matricula} y el descuento es {descuento}.")
        print(f"El valor a pagar es {valor_matricula - descuento}.")
        
elif estrato == 2:
    if edad < 18:
        descuento = valor_matricula * 0.10
        print(f"El valor de la matrícula es {valor_matricula} y el descuento es {descuento}.")
        print(f"El valor a pagar es {valor_matricula - descuento}.")
    else:
        descuento = valor_matricula * 0.05
        print(f"El valor de la matrícula es {valor_matricula} y el descuento es {descuento}.")
        print(f"El valor a pagar es {valor_matricula - descuento}.")
else:
    print(f"No aplica descuento para la matricula {valor_matricula}.")