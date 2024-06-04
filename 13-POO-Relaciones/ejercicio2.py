"""A partir del siguiente diagrama:
Realice los ajustes necesarios para que:
-En la aplicación solo se pueda tener un único Banco, aunque se le puede cambiar su nombre en cualquier momento.
-Se pueda ver la información de todos los clientes del banco incluyendo su cédula, nombre, número de cuenta, tipo y saldo.
-Se pueda ver el total de los saldos en las cuentas de ahorros.
-Se pueda ver el total de los saldos en las cuentas corrientes."""

class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

    def obtener_info(self):
        return f"Número de la cuenta: {self.numero}, Tipo de cuenta: {self.tipo}, Saldo: {self.saldo}"

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta: Cuenta):
        self.cuentas.append(cuenta)

    def obtener_cuentas(self):
        return self.cuentas

    def total_saldo_tipo(self, tipo):
        return sum(cuenta.saldo for cuenta in self.cuentas if cuenta.tipo == tipo)

class Banco:

    def __init__(self, nombre):
            self.nombre = nombre
            self.clientes = []
           

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return self.clientes

    def ver_info_clientes(self):
        for cliente in self.clientes:
            print(f"Cédula: {cliente.cedula}, Nombre: {cliente.nombre}")
            for cuenta in cliente.obtener_cuentas():
                print(f"  {cuenta.obtener_info()}")

    def total_saldos_ahorros(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.total_saldo_tipo('ahorros')
        return total

    def total_saldos_corriente(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.total_saldo_tipo('corriente')
        return total

# Comprobación de los métodos

banco = Banco("Banco Central")

cliente1 = Cliente("123456789", "Juan Pérez")
cliente2 = Cliente("987654321", "Ana Gómez")


cuenta1 = Cuenta("001", "ahorros", 1000.50)
cuenta2 = Cuenta("002", "corriente", 2500.75)
cuenta3 = Cuenta("003", "ahorros", 1500.00)
cuenta4 = Cuenta("004", "corriente", 5000.00)


cliente1.agregar_cuenta(cuenta1)
cliente1.agregar_cuenta(cuenta2)
cliente2.agregar_cuenta(cuenta3)
cliente2.agregar_cuenta(cuenta4)


banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)


banco.ver_info_clientes()

print("Total saldos en cuentas de ahorros:", banco.total_saldos_ahorros())

print("Total saldos en cuentas corrientes:", banco.total_saldos_corriente())
