# Ejercicio
# Reemplazar elementos de una lista

# Descripción del ejercicio:
# En este ejercicio, trabajarás con la lista `areas`, que contiene los nombres y áreas de diferentes habitaciones de una casa.
# Aprenderás cómo:
# 1. Reemplazar elementos individuales usando índices.
# 2. Cambiar múltiples elementos a la vez para modificar partes específicas de la lista.

# Instrucciones:
# 1. Actualiza el área del baño a 10.50 metros cuadrados en lugar de 9.50. Usa índices negativos para hacer esta actualización.
# 2. Cambia el nombre "living room" a "chill zone". No uses índices negativos esta vez.

# Código en Python:
# Crear la lista areas
areas = ["hallway", 11.25,  # Pasillo y su área.
         "kitchen", 18.0,   # Cocina y su área.
         "living room", 20.0,  # Sala de estar y su área.
         "bedroom", 10.75,  # Habitación y su área.
         "bathroom", 9.50]  # Baño y su área.

# Actualizar el área del baño usando un índice negativo
areas[-1] = 10.50  # Cambiar el último elemento (área del baño).
print("Lista después de actualizar el área del baño:", areas)

# Cambiar "living room" a "chill zone"
areas[4] = "chill zone"  # Reemplazar "living room" en el índice 4.
print("Lista después de cambiar 'living room' a 'chill zone':", areas)

# Explicación del código:
# - La línea 16 crea la lista inicial `areas`, que contiene nombres (str) y áreas (float) de diferentes habitaciones.
# - La línea 20 actualiza el último elemento de la lista usando el índice negativo `-1` para modificar el área del baño.
# - La línea 24 reemplaza el elemento en el índice 4 para cambiar el nombre "living room" a "chill zone".
# - Las líneas 21 y 25 imprimen la lista modificada después de cada cambio para verificar los resultados.

# Notas:
# - Usar índices negativos es útil para acceder rápidamente a los últimos elementos de una lista.
# - Cambiar elementos de una lista es una operación directa, pero afecta directamente la lista original.
