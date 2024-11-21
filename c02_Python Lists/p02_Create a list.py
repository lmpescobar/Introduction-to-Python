# Ejercicio
# Crear una lista en Python

# Descripción del ejercicio:
# En este ejercicio, aprenderás a crear una lista que agrupe múltiples valores relacionados.
# Las listas son un tipo de dato compuesto en Python que te permite almacenar varios valores bajo un único nombre.
# Por ejemplo:
# a = "is"
# b = "nice"
# my_list = ["my", "list", a, b]
# Puedes usar listas para organizar y agrupar datos de forma lógica.

# Contexto:
# Después de medir las alturas de tu familia, decides recolectar información sobre las áreas de tu casa.
# Las áreas de las diferentes partes de tu casa están almacenadas en variables separadas.

# Instrucciones:
# 1. Crea una lista llamada `areas` que contenga el área de las siguientes partes de la casa:
#    - Pasillo (`hall`): 11.25
#    - Cocina (`kit`): 18.0
#    - Sala de estar (`liv`): 20.0
#    - Habitación (`bed`): 10.75
#    - Baño (`bath`): 9.50
#    Asegúrate de incluirlas en este orden.
# 2. Usa las variables predefinidas `hall`, `kit`, `liv`, `bed` y `bath` para construir la lista.
# 3. Imprime la lista `areas` usando la función `print()`.

# Código en Python:
# Definir las áreas individuales como variables
hall = 11.25  # Área del pasillo en metros cuadrados.
kit = 18.0    # Área de la cocina en metros cuadrados.
liv = 20.0    # Área de la sala de estar en metros cuadrados.
bed = 10.75   # Área de la habitación en metros cuadrados.
bath = 9.50   # Área del baño en metros cuadrados.

# Crear la lista areas
areas = [hall, kit, liv, bed, bath]  # Lista que agrupa las áreas de todas las partes de la casa.

# Imprimir la lista areas
print(areas)  # Mostrar la lista completa en la consola.

# Explicación del código:
# - Las líneas 14-18 definen variables individuales que almacenan las áreas de las diferentes partes de la casa.
# - La línea 21 crea una lista llamada `areas`, que agrupa estas variables en un solo objeto.
# - La línea 24 imprime el contenido de la lista `areas`, mostrando los valores almacenados en ella.