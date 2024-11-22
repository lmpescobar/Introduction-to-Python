# Ejercicio
# Uso de múltiples argumentos en funciones

# Descripción del ejercicio:
# En este ejercicio, aprenderás cómo trabajar con la función `sorted()` de Python,
# que permite ordenar elementos en una lista. Esta función tiene múltiples argumentos:
# 1. `iterable`: Los datos a ordenar (obligatorio).
# 2. `key`: Una función opcional que especifica cómo ordenar los elementos.
# 3. `reverse`: Un argumento opcional para especificar si deseas ordenar en orden descendente.

# Instrucciones:
# 1. Combina las listas `first` y `second` usando el operador `+` y almacénalas en `full`.
# 2. Usa `sorted()` en la lista `full` y pasa el argumento `reverse=True` para ordenar en orden descendente.
# 3. Guarda la lista ordenada como `full_sorted`.
# 4. Imprime la lista `full_sorted`.

# Código en Python:
# Crear las listas first y second
first = [11.25, 18.0, 20.0]  # Lista de números flotantes.
second = [10.75, 9.50]       # Otra lista de números flotantes.

# Combinar las listas first y second
full = first + second  # Unir las dos listas en una sola.
print("Lista combinada (full):", full)  # Mostrar la lista combinada.

# Ordenar la lista full en orden descendente
full_sorted = sorted(full, reverse=True)  # Ordenar en orden descendente.
print("Lista ordenada en orden descendente (full_sorted):", full_sorted)

# Explicación del código:
# - La línea 16 crea una nueva lista combinando `first` y `second` con el operador `+`.
# - La línea 19 usa la función `sorted()` para ordenar la lista combinada:
#   - `iterable=full`: Especifica la lista a ordenar.
#   - `reverse=True`: Indica que el orden debe ser descendente.
# - La línea 22 imprime la lista ordenada para verificar el resultado.

# Notas adicionales:
# - La función `sorted()` no modifica la lista original. En su lugar, devuelve una nueva lista ordenada.
# - El argumento `reverse` es opcional; si no se especifica, el orden es ascendente por defecto.
# - Puedes usar el argumento `key` para personalizar el criterio de ordenación, como ordenar por longitud o por valores absolutos.