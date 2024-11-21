# Ejercicio
# Manipulación de listas en Python

# Descripción del ejercicio:
# En este ejercicio, aprenderás cómo manipular listas en Python. Esto incluye:
# 1. Cambiar elementos de una lista.
# 2. Agregar nuevos elementos.
# 3. Eliminar elementos.
# 4. Comprender cómo funcionan las listas en Python "detrás de escena".

# Conceptos clave:
# - Cambiar elementos: Usa índices o slices con corchetes y el signo igual para actualizar valores.
# - Agregar elementos: Usa el operador `+` para combinar listas.
# - Eliminar elementos: Usa `del` para remover elementos específicos.
# - Copiar listas: La asignación `=` crea referencias, no copias independientes.

# Código en Python:
# Crear la lista original `fam`
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# Cambiar elementos de la lista
# Actualizar la altura de "dad" a 1.86
fam[7] = 1.86  # Cambiar el último elemento
print("Lista después de actualizar la altura de 'dad':", fam)

# Cambiar un slice completo
# Actualizar "liz" y su altura
fam[0:2] = ["lisa", 1.74]
print("Lista después de cambiar 'liz' a 'lisa':", fam)

# Agregar elementos a la lista
# Añadir tu propio nombre y altura
fam_ext = fam + ["me", 1.79]
print("Lista después de agregar tu nombre y altura:", fam_ext)

# Eliminar elementos de la lista
# Eliminar "emma" y su altura
del fam[2]  # Elimina "emma"
del fam[2]  # Elimina la altura de "emma"
print("Lista después de eliminar a 'emma' y su altura:", fam)

# Detrás de escena: referencias y copias
# Crear una nueva lista `x`
x = ["a", "b", "c"]
# Copiar `x` en `y` usando el signo igual
y = x
# Cambiar un elemento en `y`
y[1] = "z"
print("Lista x después de modificar y:", x)  # Cambia también en `x`

# Crear una copia independiente de la lista
z = list(x)  # Usar la función `list`
z[1] = "y"
print("Lista x después de modificar una copia independiente:", x)  # No cambia en `x`
print("Lista z independiente:", z)

# Explicación del código:
# - Las líneas 16-17 actualizan un elemento específico usando un índice.
# - Las líneas 20-21 actualizan un slice de la lista, reemplazando los primeros dos elementos.
# - Las líneas 24-25 combinan `fam` con otra lista usando el operador `+`.
# - Las líneas 28-29 eliminan dos elementos consecutivos usando `del`.
# - Las líneas 33-39 muestran cómo el signo igual crea una referencia, no una copia, lo que significa que los cambios en `y` afectan a `x`.
# - Las líneas 42-45 crean una copia independiente con la función `list`, lo que garantiza que los cambios en `z` no afectan a `x`.

# Practica:
# Experimenta cambiando otros elementos, agregando diferentes datos o copiando listas de diversas maneras.