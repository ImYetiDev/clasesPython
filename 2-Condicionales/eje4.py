peso = float(input("Ingrese el peso del paquete en kg: "))
destino = input("Ingrese el destino del envío - nacional o internacional: ")
if destino == 'nacional':
    if peso <= 3:
        costo = 29340
    elif peso <= 7:
        costo = 55740
    elif peso <= 10:
        costo = 75540
    elif peso <= 15:
        costo = 108540
    elif peso <= 20:
        costo = 141540
    else:
        costo = 141540 + (peso - 20) * 6840
elif destino == 'internacional':
    if peso <= 3:
        costo = 46380
    elif peso <= 7:
        costo = 100380
    elif peso <= 10:
        costo = 132780
    elif peso <= 15:
        costo = 186780
    elif peso <= 20:
        costo = 240780
    else:
        costo = 240780 + (peso - 20) * 12000
else:
    print("Destino no válido.")
    costo = None

if costo is not None:
    print("El costo de envío es: ${:.2f} COP".format(costo))
