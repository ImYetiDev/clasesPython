lista_salomia = set (['deportes', 'musica','robó5tica','pintura','danza'])
lista_norte = set(['danza', 'fotografía', 'arte', 'música', 'robótica', 'arte', 'taller lectura', 'música',
'robótica','danza'])
lista_tequedama = set( ['teatro', 'danza', 'ajedrez', 'robótica', 'deportes', 'taller lectura', 'club ciencias'])
x= lista_salomia.union(lista_tequedama.union(lista_norte))

print(F"estas son totas las actividades propuestas:={x} ")

print(f"estas son las actividades en comun con las sedes: = {lista_salomia.intersection(lista_norte,lista_tequedama)}")

print(f"estas son las sedes que las quiere cada sede = ")