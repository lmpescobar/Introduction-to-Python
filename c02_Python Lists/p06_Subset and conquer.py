# Ejercicio
# Subsetting y acceder a elementos en una lista

# Descripción del ejercicio:
# Subsetting en Python es muy sencillo. Este ejercicio te permitirá practicar cómo acceder a elementos
# específicos de una lista usando índices positivos y negativos. La lista `areas` incluye nombres y áreas de
# diferentes partes de una casa. Tu objetivo es usar subsetting para imprimir elementos específicos de la lista.

# Instrucciones:
# 1. Imprime el segundo elemento de la lista `areas` (que tiene el valor 11.25).
# 2. Usa un índice negativo para imprimir el último elemento de la lista `areas` (valor 9.50).
# 3. Imprime el número que representa el área de la sala de estar (20.0) desde la lista `areas`.

# Código en Python:
# Crear la lista areas
areas = ["hallway", 11.25,  # Pasillo y su área.
         "kitchen", 18.0,   # Cocina y su área.
         "living room", 20.0,  # Sala de estar y su área.
         "bedroom", 10.75,  # Habitación y su área.
         "bathroom", 9.50]  # Baño y su área.

# Imprimir el segundo elemento de la lista
print(areas[1])  # Índice 1: Área del pasillo (11.25).

# Imprimir el último elemento de la lista usando un índice negativo
print(areas[-1])  # Índice -1: Área del baño (9.50).

# Imprimir el área de la sala de estar
print(areas[5])  # Índice 5: Área de la sala de estar (20.0).

# Explicación del código:
# - La línea 14 crea la lista `areas`, que incluye nombres (str) y áreas (float) de diferentes habitaciones.
# - La línea 18 usa el índice 1 para acceder al segundo elemento de la lista (11.25).
# - La línea 21 usa el índice -1 para acceder al último elemento de la lista (9.50).
# - La línea 24 usa el índice 5 para acceder al área de la sala de estar (20.0), que corresponde a su posición en la lista.