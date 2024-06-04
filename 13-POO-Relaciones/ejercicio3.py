"""Implemente dos relaciones de herencia al ejercicio anterior creando una clase CuentaAhorro y otra CuentaCorriente que hereden de laclase Cuenta. Elimine el atributo tipo de la clase Cuenta y agregue a la clase CuentaAhorro un atributo llamado interés con un métodoaplicar_interes que incrementa el saldo en el interés dado y a la CuentaCorriente incluir un atributo llamado descuento con un métodoaplicar_descuento que disminuye el saldo el descuento dado. La aplicación debe continuar funcionando con los ajustes dados."""

class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    
    def obtener_info(self):
        return f"Cuenta {self.numero}, Saldo: {self.saldo}"

class CuentaAhorro(Cuenta):
    def __init__(self, numero, saldo, interes):
        super().__init__(numero, saldo)
        self.interes = interes
    
    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes
    
    def obtener_info(self):
        return f"Cuenta de Ahorros {self.numero}, Saldo: {self.saldo}, Interés: {self.interes}"

class CuentaCorriente(Cuenta):
    def __init__(self, numero, saldo, descuento):
        super().__init__(numero, saldo)
        self.descuento = descuento
    
    def aplicar_descuento(self):
        self.saldo -= self.descuento
    
    def obtener_info(self):
        return f"Cuenta Corriente {self.numero}, Saldo: {self.saldo}, Descuento: {self.descuento}"

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuentas = []
    
    def agregar_cuenta(self, cuenta: Cuenta):
        self.cuentas.append(cuenta)
    
    def obtener_cuentas(self):
        return self.cuentas
    
    def total_saldo_tipo(self, tipo_cuenta):
        total = 0
        for cuenta in self.cuentas:
            if isinstance(cuenta, tipo_cuenta):
                total += cuenta.saldo
        return total

class Banco:
    _instance = None

    def __new__(cls, nombre):
        if cls._instance is None:
            cls._instance = super(Banco, cls).__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.clientes = []
        else:
            cls._instance.nombre = nombre
        return cls._instance

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return self.clientes
    
    def ver_info_clientes(self):
        info = []
        for cliente in self.clientes:
            for cuenta in cliente.obtener_cuentas():
                info.append(f"Cédula: {cliente.cedula}, Nombre: {cliente.nombre}, {cuenta.obtener_info()}")
        return "\n".join(info)

    def total_saldos_tipo(self, tipo_cuenta):
        total = 0
        for cliente in self.clientes:
            total += cliente.total_saldo_tipo(tipo_cuenta)
        return total

    def total_saldos_ahorros(self):
        return self.total_saldos_tipo(CuentaAhorro)
    
    def total_saldos_corriente(self):
        return self.total_saldos_tipo(CuentaCorriente)

# Ejemplo de uso:
banco = Banco("Mi Banco Único")

cliente1 = Cliente("123", "Juan Pérez")
cliente1.agregar_cuenta(CuentaAhorro("001", 1000, 0.05))
cliente1.agregar_cuenta(CuentaCorriente("002", 500, 50))

cliente2 = Cliente("456", "Ana Gómez")
cliente2.agregar_cuenta(CuentaAhorro("003", 2000, 0.03))
cliente2.agregar_cuenta(CuentaCorriente("004", 1500, 100))

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

# Aplicar intereses y descuentos
for cliente in banco.obtener_clientes():
    for cuenta in cliente.obtener_cuentas():
        if isinstance(cuenta, CuentaAhorro):
            cuenta.aplicar_interes()
        elif isinstance(cuenta, CuentaCorriente):
            cuenta.aplicar_descuento()

print(banco.ver_info_clientes())
print(f"Total en cuentas de ahorros: {banco.total_saldos_ahorros()}")
print(f"Total en cuentas corrientes: {banco.total_saldos_corriente()}")
