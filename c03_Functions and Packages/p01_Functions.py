# Ejercicio
# Introducción a las funciones en Python

# Descripción del ejercicio:
# Las funciones son bloques de código reutilizables diseñados para realizar tareas específicas.
# Ya has utilizado funciones como `type` y `max` en Python. En este ejercicio, explorarás cómo las funciones
# hacen que tu código sea más eficiente y fácil de usar. Aprenderás cómo:
# 1. Usar funciones predefinidas como `max` y `round`.
# 2. Entender qué son los argumentos de una función y cómo funcionan.
# 3. Consultar la documentación de una función con `help`.

# Conceptos clave:
# - Una función toma argumentos (inputs) y realiza una tarea.
# - Una función puede devolver un resultado (output), que puedes almacenar en una variable.
# - Los argumentos pueden ser obligatorios u opcionales, dependiendo de la función.

# Ejemplo 1: Usar funciones predefinidas
# Crear una lista de alturas de familiares
fam = [1.73, 1.68, 1.71, 1.89]  # Lista de alturas en metros.

# Usar la función `max` para obtener el valor máximo
tallest = max(fam)  # Encuentra el valor más alto en la lista `fam`.
print("La altura más alta es:", tallest)  # Mostrar el resultado.

# Explicación:
# - `max` es una función que toma una lista como argumento y devuelve el valor máximo.
# - No necesitas escribir código manual para encontrar el máximo, ya que `max` lo hace por ti.

# Ejemplo 2: Usar la función `round`
# Redondear un número a un decimal
rounded_number = round(1.68, 1)  # Redondea 1.68 a un decimal.
print("1.68 redondeado a un decimal es:", rounded_number)

# Llamar a `round` con un solo argumento
rounded_to_int = round(1.68)  # Redondea al entero más cercano.
print("1.68 redondeado al entero más cercano es:", rounded_to_int)

# Explicación:
# - `round` toma dos argumentos:
#   1. El número que deseas redondear.
#   2. El número de decimales (opcional). Si no se especifica, redondea al entero más cercano.

# Ejemplo 3: Usar `help` para explorar la documentación de una función
# Consultar la documentación de `round`
help(round)  # Muestra información sobre cómo usar `round`.

# Explicación:
# - La función `help` te permite explorar los detalles de una función.
# - En el caso de `round`, los argumentos son:
#   - `number`: El número que deseas redondear.
#   - `ndigits`: (opcional) La precisión con la que deseas redondear.

# Ejemplo 4: Almacenar resultados de funciones en variables
# Asignar el resultado de `max` a una variable
tallest = max(fam)  # Guardar el valor máximo en `tallest`.
print("La altura más alta guardada en una variable es:", tallest)

# Conceptos adicionales:
# - Los argumentos que pasas a una función se asignan a parámetros dentro de la función.
# - En `round(1.68, 1)`, el argumento `1.68` se asigna a `number` y `1` a `ndigits`.
# - Cuando un argumento opcional no se especifica, la función utiliza un valor predeterminado.

# Ejemplo 5: Argumentos opcionales en funciones
# Llamar a `round` sin especificar `ndigits`
default_round = round(2.675)
print("2.675 redondeado con el argumento predeterminado es:", default_round)

# Resumen:
# - Las funciones en Python simplifican tareas comunes.
# - Puedes usar argumentos para personalizar el comportamiento de una función.
# - Usa `help` para aprender cómo funcionan las funciones y qué argumentos aceptan.
# - Si una tarea parece común, es probable que Python ya tenga una función que lo haga.

# Consejo:
# Busca en la documentación o en internet para encontrar funciones útiles para tus tareas.
# Esto te permitirá escribir código más limpio y eficiente.