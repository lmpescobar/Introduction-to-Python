# Ejercicio
# Tu primer array en NumPy

# Descripción del ejercicio:
# En este ejercicio, aprenderás cómo crear un array de NumPy a partir de una lista de Python
# y cómo verificar el tipo de datos de este array. Trabajaremos con una lista llamada `baseball`
# que representa las alturas de jugadores de béisbol en centímetros.

# Instrucciones:
# 1. Importa la biblioteca `numpy` como `np` para usarla fácilmente en el código.
# 2. Usa la función `np.array()` para convertir la lista `baseball` en un array de NumPy. 
#    Asigna este array a la variable `np_baseball`.
# 3. Usa la función `type()` para imprimir el tipo de datos de `np_baseball`.

# Código en Python:
# Importar la biblioteca numpy como np
import numpy as np

# Lista de alturas de jugadores de béisbol en centímetros
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Crear un array de NumPy a partir de la lista baseball
np_baseball = np.array(baseball)  # Convierte la lista a un array de NumPy

# Imprimir el tipo de datos del array np_baseball
print(type(np_baseball))  # Verifica que np_baseball es un array de NumPy

# Explicación del código:
# - Línea 13: Importamos la biblioteca NumPy como `np` para facilitar su uso en el código.
# - Línea 16: Definimos la lista `baseball` que contiene las alturas de los jugadores.
# - Línea 19: Convertimos la lista `baseball` en un array de NumPy usando `np.array()`.
# - Línea 22: Imprimimos el tipo de datos de `np_baseball` usando la función `type()`.

# Notas adicionales:
# - `np.array()` es la forma estándar de convertir listas de Python a arrays de NumPy.
# - El tipo de datos del array será `<class 'numpy.ndarray'>`, que indica que se trata de un array de NumPy.

# Práctica adicional:
# - Intenta crear arrays de NumPy a partir de listas que contengan diferentes tipos de datos,
#   como enteros y flotantes, y verifica cómo NumPy maneja los tipos.
# - Usa métodos como `np_baseball.shape` para explorar las dimensiones del array.