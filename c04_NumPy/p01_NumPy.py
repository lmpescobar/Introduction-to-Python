# Ejercicio
# Introducción a NumPy

# Descripción del tema:
# - Las listas en Python son útiles y pueden contener múltiples tipos de datos. 
#   Sin embargo, no están diseñadas para realizar operaciones matemáticas elementales de forma eficiente.
# - NumPy (Numeric Python) es una biblioteca que introduce el tipo `array`, que permite realizar cálculos matemáticos
#   sobre todos los elementos de un array de manera simultánea y rápida.

# Instrucciones:
# 1. Usa NumPy para crear arrays a partir de listas de alturas y pesos.
# 2. Calcula el Índice de Masa Corporal (BMI) de cada persona.
# 3. Aplica subsetting a un array de BMI para extraer valores mayores a un umbral.

# Código en Python:

# Importar la biblioteca NumPy
import numpy as np

# Crear listas de altura (en metros) y peso (en kilogramos)
height = [1.73, 1.68, 1.71, 1.89, 1.79]  # Alturas de familiares
weight = [65.4, 59.2, 63.6, 88.4, 68.7]  # Pesos de familiares

# Convertir listas a arrays de NumPy
np_height = np.array(height)  # Array de NumPy para altura
np_weight = np.array(weight)  # Array de NumPy para peso

# Calcular el Índice de Masa Corporal (BMI): peso / altura^2
bmi = np_weight / np_height ** 2
print("BMI para cada persona:", bmi)  # Muestra el BMI de cada persona

# Aplicar subsetting: filtrar BMI mayor a 23
high_bmi = bmi[bmi > 23]  # Subsetting usando un array booleano
print("BMI mayores a 23:", high_bmi)

# Explicación del código:
# - Línea 18: Importa la biblioteca NumPy con el alias `np` para facilitar el uso.
# - Línea 21: Define la lista de alturas en metros.
# - Línea 22: Define la lista de pesos en kilogramos.
# - Línea 25: Convierte la lista `height` a un array NumPy.
# - Línea 26: Convierte la lista `weight` a un array NumPy.
# - Línea 29: Calcula el BMI para cada elemento del array usando operaciones elementales de NumPy.
# - Línea 33: Filtra los valores de BMI mayores a 23 utilizando un array booleano.

# Notas adicionales:
# - NumPy permite realizar operaciones matemáticas con arrays como si fueran valores únicos.
# - Los arrays de NumPy son más rápidos y eficientes que las listas de Python para cálculos numéricos.
# - Subsetting con booleanos es una forma poderosa de filtrar datos en NumPy.

# Práctica adicional:
# - Calcula los valores de BMI menores a 18.5 (bajo peso).
# - Experimenta con otras operaciones matemáticas en arrays, como sumar todos los elementos con `np.sum()` o calcular la media con `np.mean()`.