# Ejercicio
# Operaciones con otros tipos de variables

# Descripción del ejercicio:
# En Python, las variables pueden ser de diferentes tipos.
# Puedes verificar el tipo de una variable usando la función `type()`.
# Por ejemplo, para ver el tipo de una variable `a`, puedes ejecutar `type(a)`.
# Los diferentes tipos de variables tienen comportamientos distintos:
# - Sumar dos enteros o flotantes produce un resultado numérico.
# - Sumar dos cadenas produce una concatenación.
# Este ejercicio explora cómo se comportan los distintos tipos en operaciones.

# Instrucciones (Parte 1/2):
# 1. Suma las variables `savings` y `new_savings` y asigna el resultado a `total_savings`.
# 2. Usa `type()` para imprimir el tipo de dato de `total_savings`.

# Código en Python (Parte 1):
# Definir las variables savings y new_savings
savings = 100  # Cantidad inicial de ahorros.
new_savings = 40  # Ahorros adicionales.

# Calcular el total de ahorros
total_savings = savings + new_savings  # Sumar los ahorros iniciales con los nuevos.

# Imprimir el resultado de total_savings
print(total_savings)  # Mostrar el total de ahorros en la consola.

# Imprimir el tipo de total_savings
print(type(total_savings))  # Mostrar el tipo de dato de la variable total_savings.

# Explicación del código:
# - La línea 11 define la variable savings con un valor entero de 100.
# - La línea 12 define la variable new_savings con un valor entero de 40.
# - La línea 15 suma ambas variables y almacena el resultado en total_savings.
# - La línea 18 imprime el valor total de los ahorros en la consola.
# - La línea 21 usa la función type() para mostrar que total_savings es de tipo entero (int).

# Instrucciones (Parte 2/2):
# 1. Calcula la suma de la cadena `intro` consigo misma y asigna el resultado a `doubleintro`.
# 2. Muestra el valor de `doubleintro` usando `print()`. ¿El resultado fue el esperado?

# Código en Python (Parte 2):
# Definir la variable intro
intro = "Hello! How are you?"  # Cadena de texto que representa un saludo.

# Concatenar intro consigo misma
doubleintro = intro + intro  # Sumar (concatenar) la cadena intro con sí misma.

# Imprimir el resultado de doubleintro
print(doubleintro)  # Mostrar la cadena concatenada en la consola.

# Explicación del código:
# - La línea 27 define la variable intro con una cadena de texto.
# - La línea 30 concatena la cadena intro consigo misma usando el operador `+` y almacena el resultado en doubleintro.
# - La línea 33 imprime el valor resultante de doubleintro, que será la repetición de la cadena intro.