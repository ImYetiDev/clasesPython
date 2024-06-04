"""A partir del siguiente diagrama:
Cree las clases Banco y Cliente para que respondan al diagrama y compruebe cada uno de sus métodos"""

class Cliente:
  def __init__(self, cedula, nombre):
      self.cedula = cedula
      self.nombre = nombre

class Banco:
   def __init__(self,nombre):
      self.nombre = nombre
      self.clientes = []

   def adicionar_cliente(self, clientes:Cliente):
      self.clientes.append(clientes)

   def obtener_numero_clientes(self):
        return len(self.clientes)

   def obtener_clientes(self):
        return self.clientes

cliente1 = Cliente("123456789", "Juan Perez")
cliente2 = Cliente("987654321", "Maria Gomez")


banco = Banco("Banco Central")


banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

print("Número de clientes:", banco.obtener_numero_clientes())

clientes = banco.obtener_clientes()
print("Estos son los clientes del banco:")
for cliente in clientes:
    print(f" Nombre: {cliente.nombre}, Cédula: {cliente.cedula}")