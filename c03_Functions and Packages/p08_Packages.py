# Ejercicio
# Introducción a paquetes en Python

# Descripción:
# Los paquetes en Python permiten organizar y utilizar código externo para resolver problemas específicos.
# Los paquetes contienen módulos que incluyen funciones, métodos y tipos de datos para tareas particulares.
# Algunos ejemplos populares en ciencia de datos incluyen:
# - NumPy: Para trabajar eficientemente con arrays.
# - Matplotlib: Para visualización de datos.
# - Scikit-learn: Para aprendizaje automático.

# Instrucciones:
# 1. Aprende cómo instalar paquetes utilizando pip.
# 2. Experimenta con las diferentes formas de importar un paquete o módulo en Python.
# 3. Comprende las ventajas y desventajas de cada método de importación.

# Instalación de paquetes:
# Para instalar un paquete como NumPy en tu sistema, sigue estos pasos:
# 1. Descarga `get-pip.py` desde la URL oficial de pip.
# 2. Ejecuta el siguiente comando en tu terminal para instalar pip:
#    python3 get-pip.py
# 3. Luego, usa pip para instalar NumPy:
#    pip3 install numpy
# Nota: Los comandos `python3` y `pip3` aseguran que trabajas con Python versión 3.

# Importación de paquetes:
# 1. Importar un paquete completo
import numpy  # Importa todo el paquete NumPy.
array_1 = numpy.array([1, 2, 3])  # Crea un array utilizando numpy.array.
print("Array creado con numpy.array:", array_1)

# 2. Importar un paquete con un alias
import numpy as np  # Asigna un alias al paquete NumPy.
array_2 = np.array([4, 5, 6])  # Crea un array utilizando np.array.
print("Array creado con np.array:", array_2)

# 3. Importar una función específica de un paquete
from numpy import array  # Importa solo la función `array` del paquete NumPy.
array_3 = array([7, 8, 9])  # Crea un array directamente.
print("Array creado con array:", array_3)

# Ventajas y desventajas de cada método de importación:
# - Importar todo el paquete (por ejemplo, `import numpy`):
#   Ventaja: Deja claro de dónde provienen las funciones al usar `numpy.array`.
#   Desventaja: Puede ser más tedioso al escribir el prefijo (`numpy.`) repetidamente.
#
# - Usar un alias (por ejemplo, `import numpy as np`):
#   Ventaja: Es más conciso y mejora la legibilidad del código.
#   Desventaja: Puede ser confuso si se usan alias poco comunes.
#
# - Importar funciones específicas (por ejemplo, `from numpy import array`):
#   Ventaja: Permite acceder directamente a las funciones sin prefijos.
#   Desventaja: Puede ser menos claro en scripts largos, ya que no se sabe de dónde provienen las funciones.

# Nota adicional:
# En proyectos grandes o colaborativos, se prefiere importar paquetes completos o usar alias,
# ya que facilita la comprensión del código para otros desarrolladores.

# Practica:
# Experimenta instalando e importando otros paquetes como Matplotlib (`pip3 install matplotlib`)
# y utiliza sus funciones para trabajar en diferentes tipos de problemas.