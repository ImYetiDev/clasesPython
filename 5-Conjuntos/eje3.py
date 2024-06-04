Materias = ['Matematicas', 'Historia', 'Cátedra universitaria', 'Filosofía', 'Quimica','Fisica','Algebra','contabilidad', 'mercadeo', 'marketing', 'ambiental', 'geologia']
estudiante1 = {'Filosofia','Algebra','Contabilidad','Mercadeo'}
estudiante2 = {'Quimica','Algebra','Contabilidad','Matematicas'}

print (f"Las materias que ambos estudiantes tienen en comun son: {estudiante1.intersection(estudiante2)}")
print (f"Las materias que el primer estudiante ve sin su amigo son: {estudiante1.difference(estudiante2)}")
print (f"Las materias que los estudiantes tienen que ver aparte son: {estudiante1.symmetric_difference(estudiante2)}")