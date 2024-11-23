# Ejercicio
# Altura de jugadores de béisbol

# Descripción del ejercicio:
# Eres un gran fanático del béisbol. Decides llamar a la MLB (Major League Baseball) para obtener estadísticas sobre la altura de los jugadores principales.
# Te pasan datos sobre más de mil jugadores, proporcionados como una lista regular de Python llamada `height_in`.
# Esta lista expresa las alturas en pulgadas. El objetivo es crear un array de NumPy a partir de estos datos y convertir las alturas a metros.

# Instrucciones:
# 1. Crea un array de NumPy a partir de la lista `height_in`. Nombra este array como `np_height_in`.
# 2. Imprime `np_height_in`.
# 3. Multiplica `np_height_in` por `0.0254` para convertir todas las alturas de pulgadas a metros. Almacena los nuevos valores en un array llamado `np_height_m`.
# 4. Imprime `np_height_m` y verifica que los resultados tengan sentido.

# Código en Python:
# Importar NumPy
import numpy as np

# Crear un array de NumPy a partir de height_in
np_height_in = np.array(height_in)  # Convertir la lista height_in a un array de NumPy

# Imprimir np_height_in
print(np_height_in)  # Mostrar las alturas en pulgadas

# Convertir np_height_in a metros: np_height_m
np_height_m = np_height_in * 0.0254  # Multiplicar cada valor por 0.0254 para convertir a metros

# Imprimir np_height_m
print(np_height_m)  # Mostrar las alturas convertidas a metros

# Explicación del código:
# - Línea 17: Se importa el paquete NumPy como `np`, siguiendo la convención estándar.
# - Línea 20: Se crea un array de NumPy usando la función `np.array()`, a partir de la lista `height_in`.
# - Línea 23: Se imprime el array `np_height_in` para verificar su contenido.
# - Línea 26: Se convierte cada valor de `np_height_in` de pulgadas a metros mediante la multiplicación por `0.0254`.
# - Línea 29: Se imprime el array `np_height_m` con las alturas convertidas a metros.

# Notas adicionales:
# - NumPy permite realizar operaciones matemáticas sobre arrays enteros de manera eficiente.
# - `0.0254` es el factor de conversión de pulgadas a metros (1 pulgada = 0.0254 metros).
# - Verifica los resultados comparando manualmente algunos valores de entrada con sus conversiones.

# Práctica:
# Intenta realizar conversiones similares para otras unidades de medida o para otros conjuntos de datos, utilizando operaciones matemáticas en arrays de NumPy.