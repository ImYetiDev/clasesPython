ingles = {101, 102, 103, 104, 105, 106}
matematicas = {104, 105, 107, 108, 109, 110}
ciencias = {103, 104, 105, 110, 111, 112}

Estudiantes = ingles.union(ciencias,matematicas)
cantEstudiantes = len(Estudiantes)

print(f"La cantidad total de estudiantes que asistiran al evento deportivo es: {cantEstudiantes}")

print (f"Los estudiantes que estan inscritos en todos los cursos son ={ingles.intersection(ciencias,matematicas)}")

print (f"Los estudiantes que solo estan inscritos a un curso son: {ingles.symmetric_difference(ciencias).symmetric_difference(matematicas)}")

Aprendiz=int(input("que estudiante quiere comprobar su inscripcion: "))

materias =[]

if Aprendiz in ingles:
    materias.append("Ingles")
if Aprendiz in matematicas:
    materias.append("Matematicas")
if Aprendiz in ciencias:
    materias.append("Ciencias")
    
print(materias)
