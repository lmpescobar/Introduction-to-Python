# Introducción
# Bienvenido de nuevo, aspirante a Pythonista. Hasta ahora, has trabajado con diferentes tipos de datos en Python.
# Espero que hayas disfrutado tanto como yo explorando estas posibilidades.

# Ejercicio
# Tipos de datos en Python y listas

# Descripción del ejercicio:
# Python soporta varios tipos de datos básicos:
# 1. `float`: Representa números reales, como 1.73 o 3.14.
# 2. `int`: Representa números enteros, como 100 o -5.
# 3. `str`: Representa texto (cadenas de caracteres), como "Hola, mundo".
# 4. `bool`: Representa valores lógicos, que pueden ser `True` o `False`.
# Cada uno de estos tipos de datos puede ser almacenado en variables para representar un solo valor.

# Problema:
# Como científico de datos, frecuentemente trabajarás con múltiples puntos de datos.
# Por ejemplo, si deseas medir la altura de todos los miembros de tu familia, sería poco práctico crear
# una variable para cada altura. En su lugar, puedes almacenar toda esta información en una lista de Python.

# Instrucciones:
# 1. Crea una lista con las alturas de tu familia en metros: [1.73, 1.68, 1.71, 1.89].
# 2. Asigna un nombre a esta lista usando la variable `fam`.
# 3. Añade nombres para identificar a cada miembro de tu familia, combinando nombres y alturas en una lista.
# 4. Crea una lista de listas, donde cada sublista contenga el nombre y la altura de cada miembro.

# Código en Python:
# Crear una lista básica con las alturas de la familia
fam = [1.73, 1.68, 1.71, 1.89]  # Alturas en metros de cada miembro de la familia.

# Imprimir la lista
print("Alturas iniciales de la familia:", fam)

# Crear una lista que combine nombres y alturas
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]  # Nombres y alturas combinados.

# Imprimir la lista con nombres y alturas
print("Lista con nombres y alturas combinados:", fam)

# Crear una lista de listas
fam2 = [["liz", 1.73],  # Sublista para Liz.
        ["emma", 1.68],  # Sublista para Emma.
        ["mom", 1.71],   # Sublista para Mom.
        ["dad", 1.89]]   # Sublista para Dad.

# Imprimir la lista de listas
print("Lista de listas (fam2):", fam2)

# Explicación del código:
# - La línea 23 crea una lista llamada `fam` que contiene números (float) representando las alturas.
# - La línea 27 redefine `fam` para incluir nombres y alturas alternados como elementos de la lista.
# - Las líneas 31-35 crean una lista de listas (`fam2`), donde cada sublista contiene el nombre y altura de un miembro.
# - Las líneas 26, 30 y 37 imprimen el contenido de cada lista para verificar su estructura.

# Información adicional:
# En Python, las listas son muy flexibles. Pueden contener elementos de cualquier tipo, incluyendo otras listas.
# Este tipo de estructura es ideal para organizar datos complejos de manera simple.