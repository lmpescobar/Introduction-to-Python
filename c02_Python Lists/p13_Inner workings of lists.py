# Ejercicio
# Funcionamiento interno de las listas en Python

# Descripción del ejercicio:
# En Python, las listas no almacenan los valores directamente en una variable, sino que la variable actúa como una referencia
# al lugar donde los datos están almacenados en la memoria. Esto significa que al copiar una lista usando el operador `=`,
# no se crea una nueva lista, sino otra referencia a la misma lista en memoria.
# Para evitar que los cambios en una copia afecten a la lista original, debes crear una copia explícita.

# Instrucciones:
# 1. Cambia el segundo comando que crea la variable `areas_copy`, de forma que sea una copia explícita de `areas`.
# 2. Asegúrate de que los cambios en `areas_copy` no afecten a `areas`.
# 3. Imprime `areas` para verificar que no se ha modificado después de realizar los cambios en `areas_copy`.

# Código en Python:
# Crear la lista inicial areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Lista con áreas de diferentes habitaciones.

# Crear una copia explícita de areas
areas_copy = list(areas)  # Usar la función list() para crear una copia independiente.

# Modificar el primer elemento de areas_copy
areas_copy[0] = 5.0  # Cambiar el primer elemento de la copia.

# Imprimir la lista original areas
print("Lista original 'areas' después de modificar 'areas_copy':", areas)

# Explicación del código:
# - La línea 16 define la lista original `areas` con valores flotantes que representan áreas.
# - La línea 19 usa la función `list()` para crear una copia independiente de `areas` y asignarla a `areas_copy`.
# - La línea 22 modifica el primer elemento de `areas_copy`. Dado que es una copia independiente, no afecta a `areas`.
# - La línea 25 imprime la lista original `areas` para verificar que no ha cambiado.

# Notas adicionales:
# - Usar `=` crea una referencia, lo que significa que los cambios realizados en una copia afectarán a la lista original.
# - Para evitar esto, se debe usar `list()` o slicing (`[:]`) para crear copias independientes.