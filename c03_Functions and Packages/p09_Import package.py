# Ejercicio
# Importar paquetes en Python

# Descripción del ejercicio:
# Calcularás la circunferencia y el área de un círculo utilizando el paquete `math` en Python.
# En lugar de escribir manualmente el valor de π, se utilizará `math.pi`, que proporciona este valor.
# Fórmulas:
# - Circunferencia (C): C = 2πr
# - Área (A): A = πr²
# Nota: El símbolo `**` se usa para representar la exponenciación en Python. Por ejemplo, 3**4 es 3 elevado a la 4ta potencia.

# Instrucciones:
# 1. Importa el paquete `math`.
# 2. Utiliza `math.pi` para calcular la circunferencia del círculo y almacénala en la variable `C`.
# 3. Utiliza `math.pi` para calcular el área del círculo y almacénala en la variable `A`.
# 4. Imprime los resultados con mensajes descriptivos.

# Código en Python:
# Importar el paquete math
import math  # Importa el paquete que contiene funciones y constantes matemáticas.

# Calcular la circunferencia
C = 2 * math.pi * 0.43  # Calcula la circunferencia usando la fórmula C = 2πr.

# Calcular el área
A = math.pi * 0.43 ** 2  # Calcula el área usando la fórmula A = πr².

# Imprimir los resultados
print("Circumference: " + str(C))  # Imprime la circunferencia como un mensaje descriptivo.
print("Area: " + str(A))  # Imprime el área como un mensaje descriptivo.

# Explicación del código:
# - La línea 16 importa el paquete `math`, que contiene `pi` y otras constantes útiles.
# - La línea 19 calcula la circunferencia usando la fórmula matemática y almacena el resultado en `C`.
# - La línea 22 calcula el área usando la fórmula matemática y almacena el resultado en `A`.
# - Las líneas 25 y 26 convierten los valores numéricos a cadenas (`str`) para incluirlos en el mensaje impreso.

# Notas adicionales:
# - `math.pi` proporciona un valor preciso de π.
# - Usar paquetes como `math` permite cálculos matemáticos avanzados con funciones y constantes predefinidas.
# - Los valores impresos serán en formato decimal, ya que las operaciones incluyen números de punto flotante.

# Practica:
# Modifica el radio del círculo en el código y observa cómo cambian los resultados.
# Explora otras funciones útiles en el paquete `math`, como `math.sqrt()` para calcular raíces cuadradas.