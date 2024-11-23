# Importar NumPy
import numpy as np

# Simulación de datos: 5000 filas, 2 columnas (altura en metros y peso en kilogramos)
np.random.seed(42)  # Fijar una semilla para reproducibilidad
heights = np.random.normal(1.75, 0.2, 5000)  # Alturas con media 1.75 m y desviación estándar 0.2 m
weights = np.random.normal(70.0, 10.0, 5000)  # Pesos con media 70 kg y desviación estándar 10 kg

# Crear la matriz 2D np_city
np_city = np.column_stack((heights, weights))

# 1. Calcular la altura promedio
mean_height = np.mean(np_city[:, 0])  # Seleccionar la primera columna (altura) y calcular la media
print("Altura promedio (m):", mean_height)

# 2. Calcular la mediana de las alturas
median_height = np.median(np_city[:, 0])  # Calcular la mediana
print("Altura mediana (m):", median_height)

# 3. Calcular la desviación estándar de las alturas
std_height = np.std(np_city[:, 0])  # Calcular la desviación estándar
print("Desviación estándar de la altura (m):", std_height)

# 4. Calcular la correlación entre altura y peso
correlation = np.corrcoef(np_city[:, 0], np_city[:, 1])  # Correlación entre la primera y segunda columna
print("Correlación entre altura y peso:")
print(correlation)

# 5. Imprimir resumen de datos
print("\nResumen de los datos:")
print(f"- Altura promedio: {mean_height:.2f} m")
print(f"- Altura mediana: {median_height:.2f} m")
print(f"- Desviación estándar: {std_height:.2f} m")
print(f"- Correlación (altura, peso): {correlation[0, 1]:.2f}")
