precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_comprada = int(input("Ingrese la cantidad comprada: "))

total_pagar = precio_producto * cantidad_comprada


if cantidad_comprada >= 10:
    descuento = total_pagar * 0.10
    total_pagar -= descuento

print("El total a pagar es: ${:.2f}".format(total_pagar))
