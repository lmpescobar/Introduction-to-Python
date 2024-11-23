# Ejercicio
# Importación selectiva en Python

# Descripción del ejercicio:
# En este ejercicio, aprenderás a realizar una importación selectiva desde un paquete.
# En lugar de importar todo el paquete `math`, solo importarás la constante `pi`.
# Esto es útil si solo necesitas una parte específica de un paquete en tu código.

# Fórmulas:
# - Circunferencia (C): C = 2πr
# - Área (A): A = πr²

# Instrucciones:
# 1. Realiza una importación selectiva desde el paquete `math`, importando únicamente `pi`.
# 2. Usa `pi` para calcular la circunferencia del círculo y almacénala en `C`.
# 3. Usa `pi` para calcular el área del círculo y almacénala en `A`.
# 4. Imprime los resultados con mensajes descriptivos.

# Código en Python:
# Importar únicamente la constante pi del paquete math
from math import pi  # Importación selectiva: solo se importa `pi`.

# Calcular la circunferencia
C = 2 * pi * 0.43  # Calcula la circunferencia usando la fórmula C = 2πr.

# Calcular el área
A = pi * 0.43 ** 2  # Calcula el área usando la fórmula A = πr².

# Imprimir los resultados
print("Circumference: " + str(C))  # Imprime la circunferencia con un mensaje descriptivo.
print("Area: " + str(A))  # Imprime el área con un mensaje descriptivo.

# Explicación del código:
# - La línea 16 realiza una importación selectiva, trayendo únicamente la constante `pi` del paquete `math`.
# - La línea 19 calcula la circunferencia utilizando la fórmula matemática y el valor de `pi` importado.
# - La línea 22 calcula el área utilizando la fórmula matemática y el valor de `pi`.
# - Las líneas 25 y 26 convierten los valores numéricos a cadenas (`str`) para incluirlos en los mensajes impresos.

# Ventajas de la importación selectiva:
# - Reduce el espacio ocupado en la memoria al evitar cargar todo el paquete.
# - Facilita la escritura del código al omitir el prefijo del paquete (por ejemplo, `math.`).
# Desventaja:
# - Puede ser menos claro en scripts largos, ya que no se identifica fácilmente la procedencia de los elementos importados.

# Practica:
# - Prueba a importar otras funciones o constantes de `math`, como `sqrt` o `sin`.
# - Experimenta cambiando el radio del círculo y verifica cómo cambian los resultados.