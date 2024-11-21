# Ejercicio
# Crear listas con diferentes tipos de datos

# Descripción del ejercicio:
# Aunque no es muy común, las listas en Python pueden contener una mezcla de diferentes tipos de datos,
# incluyendo cadenas de texto (str), números (float) y valores booleanos (bool).
# Este ejercicio te guiará para agregar nombres de habitaciones a una lista junto con sus tamaños,
# de modo que puedas ver fácilmente tanto el nombre como el tamaño de cada habitación.

# Contexto:
# Ya has creado una lista con las áreas de las habitaciones. Ahora agregarás los nombres de las habitaciones
# a la lista, como cadenas de texto, junto con sus áreas.

# Instrucciones:
# 1. Completa el código para crear la lista `areas`. Haz que la lista contenga primero el nombre de cada
#    habitación como una cadena de texto y luego su área correspondiente.
#    Por ejemplo: "hallway", seguido del valor de la variable `hall`.
# 2. Asegúrate de agregar los nombres "hallway", "kitchen", "living room", "bedroom" y "bathroom"
#    en las posiciones apropiadas.
# 3. Imprime la lista `areas` nuevamente. ¿Es la salida más informativa esta vez?

# Código en Python:
# Definir las áreas individuales como variables
hall = 11.25  # Área del pasillo en metros cuadrados.
kit = 18.0    # Área de la cocina en metros cuadrados.
liv = 20.0    # Área de la sala de estar en metros cuadrados.
bed = 10.75   # Área de la habitación en metros cuadrados.
bath = 9.50   # Área del baño en metros cuadrados.

# Crear y adaptar la lista areas
areas = ["hallway", hall,  # Nombre y área del pasillo.
         "kitchen", kit,   # Nombre y área de la cocina.
         "living room", liv,  # Nombre y área de la sala de estar.
         "bedroom", bed,   # Nombre y área de la habitación.
         "bathroom", bath] # Nombre y área del baño.

# Imprimir la lista areas
print(areas)  # Mostrar la lista adaptada con nombres y áreas.

# Explicación del código:
# - Las líneas 14-18 definen las variables individuales que representan las áreas de las habitaciones.
# - La línea 21 crea la lista `areas`, donde cada nombre de habitación (cadena de texto) está seguido por su área correspondiente.
# - La línea 24 imprime la lista completa `areas`, que ahora incluye tanto los nombres como los tamaños de las habitaciones.