# Ejercicio
# Datos de béisbol en formato 2D

# Descripción del ejercicio:
# Tienes una lista de listas en Python donde cada sublista representa la altura y el peso de un jugador de béisbol.
# En este ejercicio, reorganizarás esta información en un array 2D de NumPy para aprovechar su funcionalidad adicional.

# Instrucciones:
# 1. Usa `np.array()` para crear un array 2D de NumPy a partir de la lista `baseball`.
#    Asigna el array resultante a la variable `np_baseball`.
# 2. Imprime el atributo `.shape` del array `np_baseball` para verificar sus dimensiones.

# Código en Python:
import numpy as np  # Importar el paquete NumPy para trabajar con arrays.

# Ejemplo de lista de datos de béisbol
baseball = [
    [180, 78.4],  # Altura (cm), Peso (kg) del primer jugador
    [215, 102.7], # Altura (cm), Peso (kg) del segundo jugador
    [210, 98.5],  # Altura (cm), Peso (kg) del tercer jugador
    [188, 75.2]   # Altura (cm), Peso (kg) del cuarto jugador
]

# Crear un array 2D de NumPy a partir de la lista de listas baseball
np_baseball = np.array(baseball)  # Convertir la lista de listas baseball a un array 2D.

# Imprimir la forma (shape) del array
print("Forma del array np_baseball:", np_baseball.shape)  # Mostrar el número de filas y columnas.

# Explicación del código:
# - Línea 15: Se importa el paquete NumPy como np para simplificar el uso de sus funciones.
# - Línea 18: La lista `baseball` contiene sublistas con datos de altura y peso de los jugadores.
# - Línea 23: La función `np.array()` convierte la lista de listas en un array 2D de NumPy.
# - Línea 26: Se usa el atributo `.shape` para imprimir las dimensiones del array (número de filas y columnas).

# Notas adicionales:
# - NumPy transforma automáticamente los datos en un formato homogéneo dentro del array.
# - El atributo `.shape` es útil para comprender la estructura de los datos.

# Práctica:
# - Intenta agregar más filas de datos a la lista `baseball` y observa cómo cambian las dimensiones del array.
# - Experimenta con operaciones matemáticas utilizando el array `np_baseball`.