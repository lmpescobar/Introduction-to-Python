# Ejercicio
# Comparación entre media y mediana en un arreglo NumPy

# Descripción del ejercicio:
# El objetivo es calcular estadísticas básicas (media y mediana) de las alturas de los jugadores de béisbol 
# almacenadas en la primera columna de un arreglo 2D de NumPy. Esto ayudará a entender cómo los valores extremos 
# (outliers) afectan las estadísticas resumen.

# Instrucciones:
# 1. Crear un arreglo NumPy 2D llamado np_baseball con datos de alturas, pesos y edades.
# 2. Extraer la primera columna del arreglo como np_height_in.
# 3. Calcular e imprimir la media de np_height_in usando la función np.mean().
# 4. Calcular e imprimir la mediana de np_height_in usando la función np.median().

# Código en Python:

# Importar el paquete numpy como np
import numpy as np

# Crear np_baseball como un arreglo 2D con datos de ejemplo (altura en pulgadas, peso en libras, edad en años)
np_baseball = np.array([
    [74, 180, 25],
    [72, 215, 30],
    [73, 210, 28],
    [75, 188, 22],
    [70, 176, 24],
    [68, 209, 27],
    [76, 200, 26]
])  # Cada fila representa un jugador, las columnas son altura, peso y edad.

# Crear np_height_in desde la primera columna de np_baseball
np_height_in = np_baseball[:, 0]  # Selecciona todas las filas y únicamente la primera columna (alturas en pulgadas).

# Calcular y imprimir la media (promedio) de np_height_in
mean_height = np.mean(np_height_in)  # Calcula la media (promedio) de las alturas.
print("La media de las alturas (en pulgadas) es:", mean_height)

# Calcular y imprimir la mediana de np_height_in
median_height = np.median(np_height_in)  # Calcula la mediana de las alturas.
print("La mediana de las alturas (en pulgadas) es:", median_height)

# Explicación del código:
# - Línea 18: Se importa el paquete NumPy con el alias `np` para acceder a sus funciones estadísticas.
# - Línea 21: Se define un arreglo 2D `np_baseball` con datos ficticios de jugadores de béisbol. Cada fila es un jugador.
# - Línea 27: `np_baseball[:, 0]` selecciona todas las filas (`:`) y la primera columna (`0`) que contiene las alturas.
# - Línea 30: `np.mean(np_height_in)` calcula la media de las alturas seleccionadas.
# - Línea 31: Se imprime el resultado de la media con un mensaje descriptivo.
# - Línea 34: `np.median(np_height_in)` calcula la mediana, es decir, el valor central de las alturas ordenadas.
# - Línea 35: Se imprime el resultado de la mediana con un mensaje descriptivo.

# Notas adicionales:
# - La media es sensible a valores extremos (outliers), mientras que la mediana no se ve tan afectada.
# - Este ejercicio ayuda a comparar estas dos estadísticas y decidir cuál es más adecuada en presencia de valores atípicos.

# Practica:
# Intenta agregar valores extremos a `np_baseball` y observa cómo afectan la media y la mediana.