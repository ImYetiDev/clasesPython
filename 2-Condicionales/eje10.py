""" Solicita al usuario que ingrese el precio de un producto y la cantidad comprada. Calcula el
total a pagar y aplica un descuento del 10% si la cantidad es mayor o igual a 10. """

precio = int(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad comprada: "))

total = precio * cantidad

if cantidad >= 10:
  total = total - (total * 0.10)
  print(f"Se aplica un descuento del 10%")
  print(f'El total a pagar es: {total}')
else:
  print("No se aplica descuento")
  print(f'El total a pagar es: {total}')