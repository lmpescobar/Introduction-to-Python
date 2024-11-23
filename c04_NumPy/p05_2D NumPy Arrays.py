# Ejercicio
# Arrays 2D en NumPy: Creación y Subconjuntos

# Descripción del ejercicio:
# Los arrays 2D en NumPy son estructuras rectangulares que permiten almacenar datos en filas y columnas.
# En este ejercicio, trabajarás con un array 2D creado a partir de una lista de listas y practicarás
# cómo acceder a diferentes elementos y subconjuntos dentro de este array.

# Instrucciones:
# 1. Crea un array 2D de NumPy utilizando una lista de listas que contenga datos de alturas (en metros)
#    y pesos (en kilogramos) de miembros de tu familia.
# 2. Imprime la forma (shape) del array para verificar las dimensiones.
# 3. Selecciona el tercer elemento de la primera fila e imprímelo.
# 4. Utiliza la notación con coma para seleccionar el mismo elemento y confirma que el resultado es el mismo.
# 5. Selecciona los datos de altura y peso del segundo y tercer miembro de la familia, e imprímelos.
# 6. Selecciona todos los pesos y calcula la suma total de estos valores.

# Código en Python:
import numpy as np  # Importar NumPy

# Crear un array 2D con datos de altura (m) y peso (kg)
np_2d = np.array([
    [1.73, 1.68, 1.71, 1.89, 1.76],  # Alturas
    [65.4, 59.2, 63.6, 88.4, 68.7]   # Pesos
])

# Imprimir la forma (shape) del array
print("Forma del array 2D:", np_2d.shape)

# Seleccionar el tercer elemento de la primera fila
third_element_first_row = np_2d[0][2]
print("Tercer elemento de la primera fila (notación doble):", third_element_first_row)

# Seleccionar el mismo elemento utilizando la notación con coma
same_element = np_2d[0, 2]
print("Tercer elemento de la primera fila (notación con coma):", same_element)

# Seleccionar alturas y pesos del segundo y tercer miembro de la familia
sub_array = np_2d[:, 1:3]  # Todas las filas, columnas 1 a 2
print("Alturas y pesos del segundo y tercer miembro:\n", sub_array)

# Seleccionar todos los pesos (segunda fila) y calcular la suma
weights = np_2d[1, :]  # Segunda fila, todas las columnas
total_weight = np.sum(weights)
print("Pesos de todos los miembros:", weights)
print("Suma total de los pesos:", total_weight)

# Explicación del código:
# - Línea 17: Se importa el paquete NumPy para trabajar con arrays.
# - Línea 20: Se crea un array 2D a partir de una lista de listas con datos de altura y peso.
# - Línea 24: Se utiliza el atributo `.shape` para obtener las dimensiones del array (filas y columnas).
# - Línea 27: Se accede al tercer elemento de la primera fila utilizando notación doble (`[0][2]`).
# - Línea 30: Se utiliza la notación con coma para acceder al mismo elemento (`[0, 2]`).
# - Línea 33: Se seleccionan las columnas 1 y 2 (segundo y tercer miembro) para todas las filas.
# - Línea 36: Se accede a todos los elementos de la segunda fila (pesos) y se calcula la suma total.

# Notas adicionales:
# - La notación `[fila, columna]` es más compacta y recomendada para trabajar con arrays de NumPy.
# - Al usar un rango como `1:3` en subsetting, el límite superior no está incluido.
# - La operación `np.sum()` permite realizar una suma eficiente de todos los elementos de un array.

# Práctica:
# Intenta crear arrays 2D con más filas y columnas y experimenta con diferentes operaciones,
# como calcular promedios o seleccionar subconjuntos específicos.