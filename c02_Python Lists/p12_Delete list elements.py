# Ejercicio
# Eliminar elementos de una lista en Python utilizando slicing y la declaración `del`

# Descripción del ejercicio:
# En este ejercicio, aprenderás a eliminar múltiples elementos consecutivos de una lista usando slicing con `del`.
# Supongamos que decides eliminar los datos relacionados con la piscina ("poolhouse") y su área de la lista `areas`.

# Instrucciones:
# 1. Usa slicing y la declaración `del` para eliminar tanto la cadena `"poolhouse"` como el número flotante `24.5` de la lista `areas`.
# 2. Imprime la lista actualizada para verificar que los elementos han sido eliminados correctamente.

# Código en Python:
# Crear la lista inicial areas
areas = ["hallway", 11.25,  # Pasillo y su área.
         "kitchen", 18.0,   # Cocina y su área.
         "chill zone", 20.0,  # Sala de estar y su área.
         "bedroom", 10.75,  # Habitación y su área.
         "bathroom", 10.50,  # Baño y su área.
         "poolhouse", 24.5,  # Piscina y su área.
         "garage", 15.45]    # Garaje y su área.

# Eliminar los elementos correspondientes a "poolhouse" y su área utilizando slicing
del areas[10:12]  # Eliminar los elementos en los índices 10 y 11.

# Imprimir la lista actualizada
print("Lista después de eliminar 'poolhouse' y su área:", areas)

# Explicación del código:
# - La línea 16 define la lista inicial `areas`, que incluye nombres y áreas de habitaciones y estructuras adicionales.
# - La línea 20 usa slicing con `del` para eliminar los elementos desde el índice 10 hasta el 11 (incluidos).
# - La línea 23 imprime la lista actualizada para verificar que los elementos han sido eliminados correctamente.

# Notas adicionales:
# - Usar slicing con `del` es una forma eficiente de eliminar varios elementos consecutivos de una lista.
# - El slicing ajusta automáticamente los índices de los elementos restantes en la lista.