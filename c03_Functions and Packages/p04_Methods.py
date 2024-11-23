# Ejercicio
# Métodos en Python

# Descripción del ejercicio:
# En Python, todo es un objeto. Esto significa que incluso tipos de datos básicos como listas, cadenas, números,
# e incluso booleanos, tienen métodos asociados. Los métodos son funciones que están "ligadas" a un objeto específico
# y se invocan utilizando la notación de punto: `objeto.metodo()`.
# En este ejercicio, aprenderás:
# 1. Qué son los métodos y cómo funcionan.
# 2. Métodos de listas, cadenas, y cómo se comportan según el tipo de objeto.
# 3. Métodos que modifican los objetos y cómo utilizarlos de manera segura.

# Conceptos clave:
# - Los métodos son funciones asociadas a un objeto específico.
# - Cada tipo de objeto tiene un conjunto único de métodos disponibles.
# - Algunos métodos devuelven un nuevo resultado sin alterar el objeto original.
# - Otros métodos modifican directamente el objeto al que se aplican.

# Ejemplo 1: Métodos de listas
# Crear la lista fam
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]  # Lista de nombres y alturas.

# Usar el método `index` para obtener la posición de un elemento
mom_index = fam.index("mom")  # Encuentra el índice de "mom" en la lista.
print("El índice de 'mom' en la lista es:", mom_index)

# Usar el método `count` para contar las veces que aparece un elemento
liz_height_count = fam.count(1.73)  # Cuenta cuántas veces aparece 1.73 en la lista.
print("El número de veces que 1.73 aparece en la lista es:", liz_height_count)

# Explicación:
# - `index` devuelve la posición del primer elemento coincidente en la lista.
# - `count` cuenta cuántas veces aparece un valor específico en la lista.

# Ejemplo 2: Métodos de cadenas
# Crear la variable sister como una cadena
sister = "elizabeth"

# Usar el método `capitalize` para poner en mayúscula la primera letra
sister_capitalized = sister.capitalize()
print("Cadena con la primera letra en mayúscula:", sister_capitalized)

# Usar el método `replace` para reemplazar partes de la cadena
sister_replaced = sister.replace("beth", "sa")
print("Cadena después de reemplazar 'beth' con 'sa':", sister_replaced)

# Explicación:
# - `capitalize` transforma la primera letra de una cadena en mayúscula.
# - `replace` reemplaza todas las ocurrencias de un texto específico por otro texto.

# Ejemplo 3: Métodos que modifican el objeto
# Usar el método `append` para agregar elementos a la lista fam
fam.append("me")  # Agregar "me" al final de la lista.
fam.append(1.75)  # Agregar mi altura a la lista.
print("Lista después de usar append:", fam)

# Explicación:
# - `append` modifica directamente la lista original agregando un elemento al final.
# - A diferencia de métodos como `index`, `append` no genera un nuevo resultado, sino que cambia el objeto en sí.

# Ejemplo 4: Métodos similares en diferentes tipos de objetos
# Crear una cadena y una lista
string_example = "hello"
list_example = ["h", "e", "l", "l", "o"]

# Usar el método `index` en una cadena
char_index = string_example.index("e")  # Encuentra el índice de "e" en la cadena.
print("El índice de 'e' en la cadena es:", char_index)

# Usar el método `index` en una lista
element_index = list_example.index("e")  # Encuentra el índice de "e" en la lista.
print("El índice de 'e' en la lista es:", element_index)

# Explicación:
# - Tanto cadenas como listas tienen el método `index`, pero su comportamiento depende del tipo de objeto.

# Ejemplo 5: Métodos y sus efectos en objetos
# Llamar al método `reverse` para invertir una lista
fam.reverse()  # Invertir los elementos de la lista.
print("Lista después de usar reverse:", fam)

# Explicación:
# - `reverse` modifica la lista directamente en lugar de devolver una nueva lista.

# Resumen:
# - Los métodos son funciones especializadas para objetos específicos.
# - Algunos métodos como `append` y `reverse` modifican el objeto directamente.
# - Otros métodos como `count` y `index` generan un resultado sin cambiar el objeto original.
# - Es importante entender el tipo de objeto al que aplicas un método, ya que esto determina qué métodos están disponibles.

# Practica:
# Intenta usar otros métodos en listas y cadenas, como `sort`, `split`, `join`, y observa cómo se comportan.