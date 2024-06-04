""" Consulte sobre algún paquete interesante en el PyPI instálelo y utilícelo en un programa. Presente el paquete usado y su
utilidad y muestre su aplicación en el programa desarrollado """

from faker import Faker

# Inicializar Faker
fake = Faker()

# Generar datos falsos
def generate_fake_data(records):
    data = []
    for _ in range(records):
        person = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
        }
        data.append(person)
    return data

fake_data = generate_fake_data(5)
for record in fake_data:
    print(record)
    print('---')
