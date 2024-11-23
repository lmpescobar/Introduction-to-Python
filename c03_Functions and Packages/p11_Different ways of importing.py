# Ejercicio
# Diferentes formas de importar en Python

# Descripción del ejercicio:
# Python permite importar paquetes y módulos de varias maneras dependiendo de cómo planeas usarlos.
# En este caso, la función `inv()` se encuentra en el subpaquete `linalg` del paquete `scipy`.
# Se desea usar esta función como `my_inv` en el código: 
# my_inv([[1, 2], [3, 4]])
# ¿Qué declaración de importación se necesita para que el código funcione sin errores?

# Instrucciones:
# Selecciona el método correcto de importación que permita usar la función `inv()` con el alias `my_inv`.

# Respuestas posibles:
# 1. import scipy
# 2. import scipy.linalg
# 3. from scipy.linalg import my_inv
# 4. from scipy.linalg import inv as my_inv

# Respuesta correcta:
# La opción correcta es:
from scipy.linalg import inv as my_inv  # Importa la función `inv` como `my_inv`.

# Explicación:
# - La línea 24 usa una importación selectiva desde el subpaquete `scipy.linalg`, trayendo solo la función `inv`.
# - La palabra clave `as` asigna un alias (`my_inv`) a la función `inv`, permitiendo usarla con este nombre.

# Código funcional:
# Importación correcta de la función inv() con alias
from scipy.linalg import inv as my_inv

# Uso de la función con el alias
resultado = my_inv([[1, 2], [3, 4]])  # Calcula la inversa de una matriz 2x2.
print("Resultado de la inversa:", resultado)

# Notas adicionales:
# - `import scipy`: Importa todo el paquete, pero no permite acceso directo a subpaquetes como `linalg`.
# - `import scipy.linalg`: Importa el subpaquete, pero necesitarás usar `scipy.linalg.inv`.
# - `from scipy.linalg import my_inv`: Incorrecto porque `my_inv` no existe en `scipy.linalg`.
# - La opción correcta usa `as` para asignar el alias y acceder directamente a la función.

# Practica:
# Intenta usar otros métodos del subpaquete `scipy.linalg`, como `det` para calcular el determinante.