# Ejercicio
# Métodos de listas en Python (Parte 2)

# Descripción del ejercicio:
# En este ejercicio, trabajarás con métodos de listas que pueden modificar la lista original:
# 1. `.append()`: Agrega un elemento al final de la lista.
# 2. `.remove()`: Elimina la primera aparición de un elemento específico en la lista.
# 3. `.reverse()`: Invierte el orden de los elementos en la lista.

# Instrucciones:
# 1. Usa el método `.append()` dos veces para agregar las áreas del "poolhouse" (24.5) y el "garage" (15.45)
#    a la lista `areas`. Asegúrate de hacerlo en este orden.
# 2. Imprime la lista `areas`.
# 3. Usa el método `.reverse()` para invertir el orden de los elementos en `areas`.
# 4. Imprime la lista `areas` nuevamente.

# Código en Python:
# Crear la lista areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Lista con áreas de diferentes partes de una casa.

# Usar .append() para agregar las áreas del poolhouse y garage
areas.append(24.5)  # Agregar el área del poolhouse.
areas.append(15.45)  # Agregar el área del garage.

# Imprimir la lista después de agregar elementos
print("Lista después de agregar poolhouse y garage:", areas)

# Usar .reverse() para invertir el orden de los elementos
areas.reverse()  # Invertir el orden de los elementos.

# Imprimir la lista después de invertir el orden
print("Lista después de invertir el orden de los elementos:", areas)

# Explicación del código:
# - La línea 16 define la lista `areas` con valores iniciales.
# - Las líneas 19-20 usan el método `.append()` para agregar los valores 24.5 y 15.45 al final de la lista.
# - La línea 23 imprime la lista `areas` después de haber agregado los nuevos elementos.
# - La línea 26 utiliza el método `.reverse()` para invertir el orden de los elementos en la lista.
# - La línea 29 imprime la lista `areas` después de invertir el orden.

# Notas adicionales:
# - `.append()` modifica directamente la lista original al agregar un nuevo elemento al final.
# - `.reverse()` también modifica la lista original invirtiendo el orden de los elementos.
# - Estos métodos son útiles cuando necesitas trabajar directamente sobre la lista existente.

# Practica:
# Intenta usar otros métodos como `.remove()` para eliminar elementos específicos
# o experimenta con combinaciones de métodos para manipular listas.