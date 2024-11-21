# Ejercicio
# Lista de listas en Python

# Descripción del ejercicio:
# Como científico de datos, a menudo trabajarás con grandes cantidades de datos.
# Para organizar mejor la información, puedes agrupar datos relacionados en una lista de listas.
# En lugar de crear una lista que combine cadenas de texto y números, representando nombres y áreas
# de las habitaciones de tu casa, puedes estructurar los datos en sublistas, donde cada sublista
# contenga un nombre y su respectiva área.

# Instrucciones:
# 1. Completa la lista `house` para que incluya los datos de las habitaciones `bedroom` y `bathroom`.
# 2. Asegúrate de que los datos de estas habitaciones estén en el orden correcto.
# 3. Imprime la lista `house`. ¿Hace que tus datos sean más comprensibles esta estructura?

# Código en Python:
# Definir las áreas individuales como variables
hall = 11.25  # Área del pasillo en metros cuadrados.
kit = 18.0    # Área de la cocina en metros cuadrados.
liv = 20.0    # Área de la sala de estar en metros cuadrados.
bed = 10.75   # Área de la habitación en metros cuadrados.
bath = 9.50   # Área del baño en metros cuadrados.

# Crear la lista de listas house
house = [["hallway", hall],    # Sublista para el pasillo.
         ["kitchen", kit],     # Sublista para la cocina.
         ["living room", liv], # Sublista para la sala de estar.
         ["bedroom", bed],     # Sublista para la habitación.
         ["bathroom", bath]]   # Sublista para el baño.

# Imprimir la lista house
print(house)  # Mostrar la estructura completa de la lista de listas.

# Explicación del código:
# - Las líneas 14-18 definen variables que representan las áreas de las diferentes partes de la casa.
# - La línea 21 crea la lista de listas `house`, donde cada sublista contiene un nombre (str) y un área (float).
# - La línea 24 imprime la lista `house`, mostrando una estructura más clara y organizada para los datos.