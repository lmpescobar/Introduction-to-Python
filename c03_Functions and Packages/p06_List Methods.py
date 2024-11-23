# Ejercicio
# Métodos de listas en Python

# Descripción del ejercicio:
# Las listas en Python tienen métodos asociados que permiten realizar operaciones útiles. En este ejercicio,
# trabajarás con los métodos:
# 1. `.index()`: Encuentra el índice del primer elemento que coincide con un valor específico.
# 2. `.count()`: Cuenta el número de veces que un elemento aparece en la lista.

# Instrucciones:
# 1. Usa el método `.index()` en la lista `areas` para encontrar el índice del elemento que es igual a 20.0.
#    Imprime este índice.
# 2. Usa el método `.count()` en la lista `areas` para contar cuántas veces aparece el número 9.50 en la lista.
#    Imprime este resultado.

# Código en Python:
# Crear la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Lista con áreas de diferentes partes de una casa.

# Usar .index() para encontrar el índice del elemento 20.0
index_of_20 = areas.index(20.0)  # Encuentra el índice del primer elemento igual a 20.0.
print("El índice del elemento 20.0 es:", index_of_20)

# Usar .count() para contar cuántas veces aparece 9.50
count_of_9_50 = areas.count(9.50)  # Cuenta las veces que 9.50 aparece en la lista.
print("El número de veces que 9.50 aparece en la lista es:", count_of_9_50)

# Explicación del código:
# - La línea 16 define una lista `areas` que contiene valores de tipo flotante.
# - La línea 19 usa el método `.index()` para encontrar la posición (índice) del primer elemento igual a 20.0.
# - La línea 20 imprime el índice encontrado.
# - La línea 23 usa el método `.count()` para contar el número de ocurrencias del valor 9.50 en la lista.
# - La línea 24 imprime el resultado del conteo.

# Notas adicionales:
# - `.index()` devuelve solo la posición del primer elemento coincidente. Si el valor no existe en la lista, genera un error.
# - `.count()` es útil para determinar la frecuencia de un valor en la lista.
# - Estos métodos no modifican la lista original; simplemente generan resultados basados en ella.

# Practica:
# Intenta aplicar estos métodos a otras listas y experimenta con valores que no existan en la lista para observar el comportamiento.