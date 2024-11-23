# Ejercicio
# Subconjuntos de arrays de NumPy

# Descripción del ejercicio:
# Trabajarás con arrays de NumPy creados a partir de dos listas: `height_in` y `weight_lb`,
# que contienen datos sobre la altura y el peso de jugadores de béisbol de la MLB.
# El objetivo es practicar la selección de subconjuntos (subsetting) de arrays de NumPy utilizando
# notación de corchetes.

# Instrucciones:
# 1. Selecciona el peso del jugador en el índice 50 del array `np_weight_lb` y imprímelo.
# 2. Obtén un subconjunto del array `np_height_in` que contenga los elementos desde el índice 100 hasta el 110 (inclusive).
#    Imprime este subconjunto.

# Código en Python:
# Importar NumPy
import numpy as np

# Crear arrays de NumPy a partir de las listas weight_lb y height_in
np_weight_lb = np.array(weight_lb)  # Convertir la lista weight_lb a un array de NumPy
np_height_in = np.array(height_in)  # Convertir la lista height_in a un array de NumPy

# Imprimir el peso del jugador en el índice 50
print("Peso del jugador en el índice 50:", np_weight_lb[50])

# Obtener un subconjunto del array np_height_in
sub_array_height = np_height_in[100:111]  # Subarray desde el índice 100 hasta el 110 (inclusive)

# Imprimir el subconjunto obtenido
print("Subarray de alturas (índices 100 a 110):", sub_array_height)

# Explicación del código:
# - Línea 17: Se importa el paquete NumPy para realizar operaciones con arrays.
# - Línea 20: Se crea un array de NumPy `np_weight_lb` a partir de la lista `weight_lb`.
# - Línea 21: Se crea un array de NumPy `np_height_in` a partir de la lista `height_in`.
# - Línea 24: Se utiliza la notación de corchetes para acceder al elemento en el índice 50 de `np_weight_lb` y se imprime.
# - Línea 27: Se obtiene un subconjunto de `np_height_in` que incluye los elementos desde el índice 100 hasta el 110 (inclusive).
# - Línea 30: Se imprime el subconjunto obtenido.

# Notas adicionales:
# - En NumPy, la notación de corchetes permite acceder a elementos individuales o subconjuntos de un array.
# - Los índices comienzan desde 0, y el límite superior del subconjunto en la notación `start:end` es exclusivo.
# - Cuando se trabaja con NumPy, las operaciones son altamente eficientes incluso para grandes conjuntos de datos.

# Práctica:
# Intenta realizar selecciones similares en arrays de NumPy con diferentes rangos de índices
# y experimenta con operaciones sobre los subconjuntos seleccionados.