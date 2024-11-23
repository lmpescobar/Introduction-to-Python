# Ejercicio
# Creación de subconjuntos de matrices NumPy 2D

# Descripción del ejercicio:
# Este ejercicio utiliza un array NumPy 2D (`np_baseball`) que contiene información sobre jugadores de béisbol.
# Aprenderás a:
# 1. Extraer una fila específica del array.
# 2. Seleccionar una columna completa del array.
# 3. Acceder a un elemento específico utilizando índices.

# Código en Python:

# Importar el paquete NumPy
import numpy as np

# Definir el array `baseball` como una lista de listas (altura y peso de los jugadores)
baseball = [
    [180, 78.4],
    [215, 102.7],
    [210, 98.5],
    [188, 75.2],
    [190, 90.1],
    [200, 95.4],
    [195, 85.6],
    [210, 105.3]
] * 20  # Repetir los datos para simular un conjunto más amplio de jugadores

# Convertir la lista `baseball` a un array NumPy 2D
np_baseball = np.array(baseball)

# 1. Imprimir la fila número 50 del array `np_baseball`
# Nota: Como NumPy usa indexación basada en cero, la fila 50 tiene índice 49.
print("Fila número 50 de np_baseball:", np_baseball[49, :])

# 2. Seleccionar la segunda columna (peso en libras) del array `np_baseball`
np_weight_lb = np_baseball[:, 1]  # Seleccionar todos los elementos de la columna 1
print("Pesos (segunda columna):", np_weight_lb)

# 3. Imprimir la altura (columna 0) del jugador número 124 (índice 123)
height_124 = np_baseball[123, 0]  # Seleccionar el valor de la fila 123, columna 0
print("Altura del jugador número 124:", height_124)

# Explicación del código:
# - Línea 17: Se importa el paquete NumPy.
# - Línea 20: Los datos ficticios de los jugadores se organizan en una lista de listas.
# - Línea 27: Se convierte la lista `baseball` a un array NumPy llamado `np_baseball`.
# - Línea 30: Se selecciona la fila número 50 (índice 49) y se imprime.
# - Línea 33: Se extrae la segunda columna completa (peso) utilizando slicing `[:, 1]`.
# - Línea 36: Se accede a la altura del jugador número 124 usando índices `[123, 0]`.

# Notas adicionales:
# - La indexación en NumPy comienza en 0. Esto significa que la primera fila tiene índice 0, la segunda índice 1, etc.
# - El slicing `:` permite seleccionar múltiples filas o columnas.
# - Al trabajar con arrays 2D, el índice antes de la coma selecciona las filas y el índice después de la coma selecciona las columnas.

# Práctica:
# - Intenta calcular el promedio de la columna de pesos (`np_weight_lb`) utilizando `np.mean(np_weight_lb)`.
# - Extrae las alturas (primera columna) de los jugadores con índices entre 100 y 110.