# Ejercicio
# Operaciones aritméticas con matrices 2D en NumPy

# Descripción del ejercicio:
# En este ejercicio, trabajarás con una matriz 2D llamada `np_baseball`, que contiene datos sobre 
# la altura (en pulgadas), el peso (en libras) y la edad (en años) de jugadores de béisbol.
# También utilizarás una matriz `conversion` para convertir las unidades de altura y peso
# a metros y kilogramos respectivamente.

# Instrucciones:
# 1. Suma las matrices `np_baseball` y `updated` para ver los cambios en los datos y muestra el resultado.
# 2. Crea un array de conversión llamado `conversion` con los valores [0.0254, 0.453592, 1].
# 3. Multiplica `np_baseball` por `conversion` para convertir las unidades y muestra el resultado.

# Código en Python:
import numpy as np  # Importar la biblioteca NumPy

# Datos iniciales: altura (pulgadas), peso (libras), edad (años)
baseball = [
    [180, 78.4, 22],
    [215, 102.7, 29],
    [210, 98.5, 25],
    [188, 75.2, 28]
]

# Crear la matriz np_baseball
np_baseball = np.array(baseball)

# Ejemplo de matriz updated: cambios en altura (pulgadas), peso (libras), edad (años)
updated = np.array([
    [2, 5.2, 0],
    [-1, -3.7, 1],
    [0, 1.2, -1],
    [1, 0.5, 0]
])

# Imprimir la suma de np_baseball y updated
print("Suma de np_baseball y updated:")
print(np_baseball + updated)

# Crear el array de conversión
conversion = np.array([0.0254, 0.453592, 1])  # Altura en metros, peso en kilogramos, edad sin cambios

# Multiplicar np_baseball por conversion y mostrar el resultado
print("\nProducto de np_baseball y conversion:")
print(np_baseball * conversion)

# Explicación del código:
# - La línea 14 convierte la lista `baseball` en una matriz NumPy 2D.
# - La línea 19 define `updated` como una matriz que contiene cambios específicos en los datos originales.
# - La línea 23 suma `np_baseball` y `updated` para reflejar las actualizaciones.
# - La línea 27 define el array `conversion` para transformar las unidades de medida.
# - La línea 30 realiza la multiplicación elemento a elemento entre `np_baseball` y `conversion`.

# Notas adicionales:
# - NumPy permite realizar operaciones elemento a elemento de forma eficiente.
# - Asegúrate de que las dimensiones sean compatibles para evitar errores.

# Practica:
# - Prueba a cambiar los valores en `updated` y `conversion` para observar cómo se transforman los datos.
# - Experimenta con otras operaciones como dividir (`/`) o calcular potencias (`**`) usando matrices NumPy.