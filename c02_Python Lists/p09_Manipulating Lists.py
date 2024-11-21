# Ejercicio
# Manipulación de listas en Python

# Descripción del ejercicio:
# Este ejercicio cubre los principales conceptos de manipulación de listas en Python:
# - Cambiar elementos específicos en una lista.
# - Modificar múltiples elementos (slicing).
# - Agregar elementos nuevos a una lista.
# - Eliminar elementos existentes.
# - Comprender cómo funcionan las referencias y copias de listas en la memoria.

# Concepto clave: Cambiar elementos en listas
# Puedes usar corchetes e índices para actualizar elementos. Por ejemplo, si la altura de "dad" en la lista `fam`
# ya no es correcta, puedes actualizarla usando el índice correspondiente.

# Crear la lista `fam` inicial
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# Cambiar un elemento específico
# Actualizar la altura de "dad" de 1.89 a 1.86
fam[7] = 1.86
print("Lista después de actualizar la altura de 'dad':", fam)

# Cambiar múltiples elementos a la vez
# Usar slicing para modificar "liz" y su altura
fam[0:2] = ["lisa", 1.74]
print("Lista después de actualizar 'liz' a 'lisa' y su altura:", fam)

# Concepto clave: Agregar elementos a una lista
# Usar el operador "+" para combinar listas
# Agregar tu propio nombre y altura
fam_ext = fam + ["me", 1.79]
print("Lista después de agregar tu nombre y altura:", fam_ext)

# Concepto clave: Eliminar elementos de una lista
# Usar `del` para eliminar un elemento basado en su índice
# Eliminar "emma" (índice 2) y su altura (índice 2 nuevamente después del primer `del`)
del fam[2]  # Eliminar "emma"
del fam[2]  # Eliminar la altura de "emma"
print("Lista después de eliminar a 'emma' y su altura:", fam)

# Concepto clave: Detrás de las escenas (Referencias y copias)
# Crear una lista `x`
x = ["a", "b", "c"]

# Asignar `x` a `y` usando el signo igual
y = x  # Esto no crea una copia, sino una referencia a la misma lista en memoria.

# Cambiar un elemento de `y`
y[1] = "z"
print("Lista x después de modificar y (referencia):", x)  # `x` también cambia.

# Crear una copia independiente de `x` usando `list()`
z = list(x)
z[1] = "y"
print("Lista x después de modificar una copia independiente:", x)  # `x` permanece igual.
print("Lista z (independiente):", z)

# Crear otra copia independiente usando slicing
w = x[:]
w[1] = "b"
print("Lista x después de modificar otra copia independiente (slicing):", x)  # `x` no cambia.
print("Lista w (independiente):", w)

# Explicación:
# - Línea 18: Se usa un índice único para actualizar el último elemento de `fam`.
# - Línea 22: Se usa slicing para reemplazar los dos primeros elementos de la lista.
# - Línea 26: Se combina `fam` con otra lista usando `+` para agregar nuevos elementos.
# - Líneas 30-32: Se elimina "emma" y su altura usando `del`, y los índices de los elementos siguientes se ajustan.
# - Líneas 36-40: Se muestra cómo una asignación con `=` crea una referencia, no una copia, afectando tanto `x` como `y`.
# - Líneas 43-44: Se crea una copia independiente usando `list()`, permitiendo cambios sin afectar la lista original.
# - Líneas 47-48: Se crea otra copia independiente con slicing (`[:]`), logrando el mismo efecto que `list()`.

# Conceptos adicionales:
# - El uso de referencias permite compartir listas en memoria, pero puede causar modificaciones inesperadas.
# - Copiar listas con `list()` o slicing (`[:]`) asegura que las listas sean independientes.