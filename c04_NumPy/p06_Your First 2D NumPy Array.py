# Ejercicio
# Tu primer array 2D de NumPy

# Descripción del ejercicio:
# En este ejercicio, trabajarás con un array 2D de NumPy creado a partir de una lista de listas. 
# Practicarás cómo crear el array, verificar su tipo y obtener su atributo de forma (shape).

# Instrucciones:
# 1. Usa `np.array()` para crear un array 2D a partir de `baseball` y asígnalo a la variable `np_baseball`.
# 2. Imprime el tipo de `np_baseball` utilizando la función `type()`.
# 3. Imprime el atributo `shape` de `np_baseball` para obtener sus dimensiones.

# Código en Python:
import numpy as np  # Importar NumPy

# Lista de listas con datos de altura (cm) y peso (kg) de jugadores de béisbol
baseball = [
    [180, 78.4],
    [215, 102.7],
    [210, 98.5],
    [188, 75.2]
]

# Crear un array 2D a partir de baseball
np_baseball = np.array(baseball)

# Imprimir el tipo del array
print("Tipo de np_baseball:", type(np_baseball))

# Imprimir la forma (shape) del array
print("Forma de np_baseball:", np_baseball.shape)

# Explicación del código:
# - Línea 14: Se importa el paquete NumPy para trabajar con arrays.
# - Línea 17: Se define una lista de listas llamada `baseball`, donde cada sublista contiene dos elementos:
#             altura (en cm) y peso (en kg) de un jugador.
# - Línea 21: Se convierte la lista `baseball` en un array 2D utilizando `np.array()`.
# - Línea 24: Se imprime el tipo de `np_baseball` para confirmar que es un array de NumPy.
# - Línea 27: Se imprime el atributo `.shape` para verificar las dimensiones del array (número de filas y columnas).

# Notas adicionales:
# - Los arrays 2D en NumPy son estructuras rectangulares que facilitan el almacenamiento y manipulación de datos tabulares.
# - El atributo `.shape` devuelve una tupla con el número de filas y columnas del array.
# - NumPy convierte automáticamente los tipos de datos en un array para garantizar la homogeneidad.

# Práctica:
# Intenta agregar más datos a la lista `baseball` y verifica cómo cambian las dimensiones y el tipo del array generado.