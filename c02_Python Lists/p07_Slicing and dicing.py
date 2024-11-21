# Ejercicio
# Slicing y selección de múltiples valores en una lista

# Descripción del ejercicio:
# Seleccionar valores individuales de una lista es solo el comienzo. También puedes "rebanar" (slice) listas,
# lo que significa seleccionar múltiples elementos y crear una nueva lista.
# Esto se logra utilizando la sintaxis:
# my_list[start:end]
# - El índice `start` está incluido en la selección.
# - El índice `end` no está incluido.
# Además, puedes omitir el índice inicial o final para simplificar la selección.

# Instrucciones:
# 1. Usa slicing para crear una lista `downstairs` que contenga los primeros 6 elementos de `areas`.
# 2. Usa slicing para crear una lista `upstairs` que contenga los últimos 4 elementos de `areas`.
#    Simplifica el slicing omitiendo el índice final.
# 3. Imprime las listas `downstairs` y `upstairs` usando `print()`.

# Código en Python:
# Crear la lista areas
areas = ["hallway", 11.25,  # Pasillo y su área.
         "kitchen", 18.0,   # Cocina y su área.
         "living room", 20.0,  # Sala de estar y su área.
         "bedroom", 10.75,  # Habitación y su área.
         "bathroom", 9.50]  # Baño y su área.

# Usar slicing para crear downstairs
downstairs = areas[:6]  # Seleccionar los primeros 6 elementos.

# Usar slicing para crear upstairs
upstairs = areas[6:]  # Seleccionar los últimos 4 elementos.

# Imprimir las listas downstairs y upstairs
print("Downstairs:", downstairs)  # Mostrar la lista downstairs.
print("Upstairs:", upstairs)      # Mostrar la lista upstairs.

# Explicación del código:
# - La línea 19 usa slicing `areas[:6]` para seleccionar los elementos desde el inicio hasta el índice 5 (6 elementos).
# - La línea 22 usa slicing `areas[6:]` para seleccionar todos los elementos desde el índice 6 hasta el final.
# - Las líneas 25-26 imprimen las listas resultantes para verificar su contenido.