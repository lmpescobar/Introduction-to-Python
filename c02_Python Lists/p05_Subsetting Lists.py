# Ejercicio
# Subsetting y slicing de listas en Python

# Descripción del ejercicio:
# Después de crear tu propia lista en Python, necesitarás acceder a información específica dentro de ella.
# Esto se logra mediante índices, los cuales permiten seleccionar elementos individuales o un rango de ellos.
# Además, aprenderás sobre slicing, que permite seleccionar múltiples elementos de una lista para crear una nueva.

# Conceptos básicos:
# - Python usa índices para acceder a los elementos de una lista.
# - El primer elemento tiene un índice 0, el segundo índice 1, y así sucesivamente.
# - También puedes usar índices negativos para contar desde el final de la lista.
# - Para obtener múltiples elementos, se utiliza la notación de slicing: [start:end].

# Instrucciones:
# 1. Usa índices para acceder a elementos específicos de la lista `fam`:
#    - Selecciona el cuarto elemento (altura de "emma").
#    - Selecciona el séptimo elemento (nombre "dad").
#    - Usa un índice negativo para seleccionar el último elemento (altura de "dad").
# 2. Practica slicing:
#    - Selecciona los elementos con índices del 3 al 4 (altura de "emma" y "mom").
#    - Selecciona los elementos con índices del 1 al 3.
#    - Omite el índice inicial para empezar desde el principio de la lista.
#    - Omite el índice final para incluir todos los elementos hasta el final.

# Código en Python:
# Crear la lista fam
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]  # Lista con nombres y alturas.

# Subsetting: acceder a elementos individuales
print(fam[3])  # Altura de "emma" (cuarto elemento, índice 3).
print(fam[6])  # Nombre "dad" (séptimo elemento, índice 6).
print(fam[-1]) # Altura de "dad" (último elemento, índice -1).

# Slicing: acceder a múltiples elementos
print(fam[3:5])  # Elementos con índices 3 y 4 (altura de "emma" y "mom").
print(fam[1:4])  # Elementos con índices 1, 2 y 3.
print(fam[:4])   # Desde el inicio hasta el índice 3.
print(fam[5:])   # Desde el índice 5 hasta el final.

# Explicación del código:
# - La línea 20 usa `fam[3]` para seleccionar el cuarto elemento (índice 3) de la lista.
# - La línea 21 usa `fam[6]` para seleccionar el séptimo elemento (índice 6).
# - La línea 22 usa `fam[-1]` para seleccionar el último elemento mediante un índice negativo.
# - La línea 25 usa `fam[3:5]` para seleccionar los elementos desde el índice 3 hasta el 4.
# - La línea 26 usa `fam[1:4]` para seleccionar los elementos desde el índice 1 hasta el 3.
# - La línea 27 usa `fam[:4]` para seleccionar todos los elementos desde el inicio hasta el índice 3.
# - La línea 28 usa `fam[5:]` para seleccionar todos los elementos desde el índice 5 hasta el final.

# Notas adicionales:
# - En slicing, el índice inicial está incluido, pero el índice final no.
# - Si omites el índice inicial, Python comienza desde el índice 0.
# - Si omites el índice final, Python incluye todos los elementos hasta el último.

# Practica:
# Intenta modificar los índices en los ejemplos anteriores para seleccionar diferentes partes de la lista.