# Ejercicio
# Exploración de datos de béisbol con estadísticas básicas usando NumPy

# Descripción del ejercicio:
# Trabajaremos con un arreglo 2D de NumPy llamado `np_baseball`, que contiene datos sobre la altura, peso 
# y edad de jugadores de béisbol. Calcularemos estadísticas básicas como media, mediana, desviación estándar 
# y la correlación entre altura y peso.

# Instrucciones:
# 1. Calcula la media de la altura (columna 0) y guárdala en `avg`.
# 2. Calcula la mediana de la altura (columna 0) y guárdala en `med`.
# 3. Calcula la desviación estándar de la altura (columna 0) usando `np.std`.
# 4. Calcula la correlación entre altura (columna 0) y peso (columna 1) con `np.corrcoef`.
# 5. Imprime los resultados con mensajes descriptivos.

# Código en Python:
import numpy as np

# Definición de datos simulados: altura (in), peso (lb), edad (años)
np_baseball = np.array([
    [180, 78.4, 25],
    [215, 102.7, 30],
    [210, 98.5, 28],
    [188, 75.2, 22],
    [176, 68.4, 19]
])

# Calcular la media de la altura (columna 0)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))  # Imprime la media

# Calcular la mediana de la altura (columna 0)
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))  # Imprime la mediana

# Calcular la desviación estándar de la altura (columna 0)
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))  # Imprime la desviación estándar

# Calcular la correlación entre altura (columna 0) y peso (columna 1)
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("Correlation: " + str(corr))  # Imprime la correlación

# Explicación del código:
# - Línea 20: `np_baseball` es un arreglo 2D que simula datos de béisbol.
# - Línea 25: Calcula la media de la altura usando `np.mean()`.
# - Línea 29: Calcula la mediana de la altura con `np.median()`.
# - Línea 33: Calcula la desviación estándar de la altura con `np.std()`.
# - Línea 37: Calcula la correlación entre altura y peso con `np.corrcoef()`.

# Notas adicionales:
# - La correlación es útil para identificar relaciones lineales entre variables.
# - Puedes ajustar los datos en `np_baseball` para observar cómo cambian los resultados.

# Practica:
# Modifica el conjunto de datos o añade nuevas columnas para explorar más estadísticas.
