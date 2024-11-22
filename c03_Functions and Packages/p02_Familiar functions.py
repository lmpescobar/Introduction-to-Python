# Ejercicio
# Funciones comunes en Python

# Descripción del ejercicio:
# Python ofrece muchas funciones integradas que facilitan tareas comunes, como:
# - Determinar el tipo de un dato con `type`.
# - Obtener la longitud de una lista con `len`.
# - Convertir tipos de datos con funciones como `int`, `str`, `float`, `bool`, etc.
# Este ejercicio te guiará para practicar estas funciones y entender cómo usarlas.

# Instrucciones:
# 1. Usa `print` en combinación con `type` para imprimir el tipo de `var1`.
# 2. Usa `len` para obtener la longitud de la lista `var1`. Envuélvelo dentro de `print` para mostrar el resultado.
# 3. Usa `int` para convertir `var2` en un entero y almacénalo en `out2`.

# Código en Python:
# Crear las variables var1 y var2
var1 = [1, 2, 3, 4]  # Lista con números enteros.
var2 = True          # Variable booleana con valor True.

# Imprimir el tipo de var1
print("El tipo de var1 es:", type(var1))  # Muestra que var1 es una lista.

# Imprimir la longitud de var1
print("La longitud de var1 es:", len(var1))  # Muestra que la lista tiene 4 elementos.

# Convertir var2 en un entero
out2 = int(var2)  # Convierte el valor booleano True en 1.
print("El valor de var2 convertido a entero es:", out2)

# Explicación del código:
# - La línea 14 usa `type` para determinar que `var1` es de tipo lista (<class 'list'>).
# - La línea 17 usa `len` para calcular la cantidad de elementos en la lista `var1` (4 en este caso).
# - La línea 20 convierte el valor booleano `var2` en un entero:
#   - En Python, `True` se convierte en `1` y `False` en `0`.

# Notas adicionales:
# - Estas funciones integradas son herramientas clave para realizar tareas comunes en Python.
# - La conversión de tipos con funciones como `int`, `float` o `str` es muy útil al trabajar con datos heterogéneos.