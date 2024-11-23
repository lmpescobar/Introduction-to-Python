# Ejercicio
# Métodos de cadenas en Python

# Descripción del ejercicio:
# Las cadenas en Python vienen con varios métodos incorporados que te permiten realizar operaciones comunes.
# Este ejercicio explora los métodos `.upper()` y `.count()` aplicados a cadenas.
# Aprenderás cómo:
# 1. Transformar una cadena a mayúsculas con `.upper()`.
# 2. Contar la cantidad de ocurrencias de un carácter específico con `.count()`.

# Instrucciones:
# 1. Usa el método `.upper()` en la variable `place` y guarda el resultado en `place_up`.
# 2. Imprime tanto `place` como `place_up`. ¿Ambos cambiaron?
# 3. Usa el método `.count()` en `place` para contar cuántas veces aparece la letra `"o"`.
#    Imprime el resultado.

# Código en Python:
# Crear una cadena para experimentar: place
place = "poolhouse"  # Cadena inicial.

# Usar el método .upper() en place
place_up = place.upper()  # Convertir toda la cadena a mayúsculas.

# Imprimir place y place_up
print("Cadena original (place):", place)  # Mostrar la cadena original.
print("Cadena en mayúsculas (place_up):", place_up)  # Mostrar la cadena en mayúsculas.

# Contar el número de "o" en place usando .count()
o_count = place.count("o")  # Contar cuántas veces aparece "o" en la cadena.

# Imprimir el número de "o" en place
print("Número de 'o' en la cadena (place):", o_count)

# Explicación del código:
# - La línea 16 define la cadena inicial `place`.
# - La línea 19 aplica el método `.upper()` a `place`, generando una nueva cadena `place_up` con todas las letras en mayúsculas.
# - La línea 22 muestra que `place` no se modifica porque `.upper()` no cambia la cadena original; genera una nueva.
# - La línea 25 usa el método `.count()` para contar el número de veces que aparece el carácter `"o"` en `place`.
# - La línea 28 imprime el resultado del conteo.

# Notas adicionales:
# - `.upper()` devuelve una nueva cadena en mayúsculas; no modifica la cadena original.
# - `.count()` es útil para contar ocurrencias de caracteres o subcadenas específicas.
# - Puedes explorar más métodos de cadenas usando `help(str)` o consultando la documentación oficial de Python.

# Practica:
# Experimenta con otros métodos de cadenas como `.lower()`, `.replace()`, `.find()`, y observa cómo funcionan.