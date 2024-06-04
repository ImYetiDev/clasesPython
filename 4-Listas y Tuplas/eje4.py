nombre = ["Jorge", "Maria", "Sandra", "David"]
edad = [25, 30, 18, 20]
sexo = ["Masculino","Femenino","Femenino","Masculino"]

pjoven = edad.index(min(edad))
perjoven = nombre[pjoven]
eperjoven = min(edad)

pmayor = edad.index(max(edad))
permayor = nombre[pmayor]
epermayor = max(edad)

num_hombres = sexo.count("Masculino")
num_mujeres = sexo.count("Femenino")

print (f"La persona mas joven es {perjoven} con {eperjoven} años de edad")
print (f"La persona con mas edad es {permayor} con {epermayor} años de edad")
print (f"Hay {num_hombres} hombres y {num_mujeres} mujeres")