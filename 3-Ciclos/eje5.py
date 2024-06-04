""" La secuencia Fibonacci es una serie de números en la que cada término es la suma de los
dos términos anteriores. La secuencia comienza con 0 y 1, y luego cada término sucesivo se
calcula sumando los dos términos anteriores. Por ejemplo, el tercer término es la suma de los
dos términos anteriores (0 + 1), por lo que es 1. El cuarto término es la suma de los dos
términos anteriores (1 + 1), por lo que es 2. Y así sucesivamente.
Elabore un algoritmo que Genere los primeros 20 términos de la secuencia Fibonacci (0, 1, 1,
2, 3, 5, 8, 13, 21, ...) """

# Algoritmo:

# 1. Inicializar las variables a = 0, b = 1, c = 0
# 2. Imprimir a
# 3. Para i en el rango de 0 a 20
# 4. c = a + b
# 5. Imprimir c
# 6. a = b
# 7. b = c
# 8. Fin Para

# Implementación en Python:

a, b, c = 0, 1, 0
print(a)

for i in range(0, 20):
    c = a + b
    print(c)
    a, b = b, c