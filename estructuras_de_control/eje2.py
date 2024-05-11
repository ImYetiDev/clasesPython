""" Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad. Si
el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la
matrícula. 
Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. 
Si el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la
edad es 18 años o mas, el descuento será del 5%.
Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento. """

edad = int(input('Ingresa tu edad: '))
estrato = int(input('Ingresa tu estrato: '))
matricula = int(input('Ingrese el costo de su matricula: '))

if edad >= 18 and estrato == 1:
    descuento = (matricula * .15)
    print(f'Aplica para descuento de 15%: Ahorrando {descuento} de la matricula original {matricula}')

elif edad < 18 and estrato == 2:
    descuento = (matricula * .10)
    print(f'Aplica para descuento de 10%: Ahorrando {descuento} de la matricula original {matricula}')
    
elif edad >= 18 and estrato == 2:
    descuento = (matricula * .05)
    print(f'Aplica para descuento de 5%: Ahorrando {descuento} de la matricula original {matricula}')
    
else:
    print(f'No aplica para descuento debe pagar el total de la matricula: {matricula}')