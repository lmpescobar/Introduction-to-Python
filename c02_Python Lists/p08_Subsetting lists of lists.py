# Ejercicio
# Subsetting listas de listas

# Descripción del ejercicio:
# Una lista en Python también puede contener otras listas, conocidas como listas anidadas.
# Para acceder a elementos dentro de estas listas anidadas, puedes usar el mismo enfoque que antes: corchetes.
# Por ejemplo, si tienes una lista `house`, puedes acceder al primer elemento de la segunda sublista usando:
# house[1][0]

# Instrucciones:
# 1. Usa subsetting para acceder a la lista `house` y obtener el valor flotante `9.5`, que corresponde al área del baño.
#    Este valor se encuentra dentro de la última sublista.

# Código en Python:
# Crear la lista anidada house
house = [["hallway", 11.25],  # Pasillo y su área.
         ["kitchen", 18.0],   # Cocina y su área.
         ["living room", 20.0],  # Sala de estar y su área.
         ["bedroom", 10.75],  # Habitación y su área.
         ["bathroom", 9.50]]  # Baño y su área.

# Acceder al área del baño (9.5) usando subsetting
bathroom_area = house[4][1]  # Seleccionar la última sublista (índice 4) y su segundo elemento (índice 1).

# Imprimir el área del baño
print(bathroom_area)  # Mostrar el valor 9.5 en la consola.

# Explicación del código:
# - La línea 15 define la lista `house`, que contiene sublistas con los nombres y áreas de las habitaciones.
# - La línea 19 usa `house[4][1]` para acceder al segundo elemento de la sublista con índice 4, que es el área del baño (9.5).
# - La línea 22 imprime el valor extraído para verificar que el subsetting fue exitoso.