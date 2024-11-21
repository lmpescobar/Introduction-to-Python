# Ejercicio
# Extender una lista en Python

# Descripción del ejercicio:
# En este ejercicio, aprenderás cómo agregar elementos a una lista utilizando el operador `+`.
# Supongamos que ganas la lotería y decides construir una piscina (poolhouse) y un garaje (garage).
# Agregarás esta información a la lista `areas` de manera progresiva.

# Instrucciones:
# 1. Usa el operador `+` para añadir la lista `["poolhouse", 24.5]` al final de `areas`. 
#    Guarda la lista resultante como `areas_1`.
# 2. Extiende aún más `areas_1` añadiendo información sobre el garaje: la cadena `"garage"` y el número flotante `15.45`.
#    Guarda la nueva lista como `areas_2`.
# 3. Imprime ambas listas (`areas_1` y `areas_2`) para verificar los resultados.

# Código en Python:
# Crear la lista inicial areas
areas = ["hallway", 11.25,  # Pasillo y su área.
         "kitchen", 18.0,   # Cocina y su área.
         "chill zone", 20.0,  # Sala de estar (anteriormente "living room") y su área.
         "bedroom", 10.75,  # Habitación y su área.
         "bathroom", 10.50]  # Baño y su área.

# Agregar datos de la piscina (poolhouse)
areas_1 = areas + ["poolhouse", 24.5]  # Añadir una piscina y su área.
print("Lista después de agregar el poolhouse:", areas_1)

# Agregar datos del garaje (garage)
areas_2 = areas_1 + ["garage", 15.45]  # Añadir un garaje y su área.
print("Lista después de agregar el garage:", areas_2)

# Explicación del código:
# - La línea 16 crea la lista inicial `areas`, que incluye nombres y áreas de las habitaciones existentes.
# - La línea 19 usa el operador `+` para combinar `areas` con otra lista que contiene la piscina y su área,
#   y guarda el resultado en `areas_1`.
# - La línea 22 usa el operador `+` nuevamente para combinar `areas_1` con otra lista que contiene el garaje
#   y su área, creando la lista final `areas_2`.
# - Las líneas 20 y 23 imprimen las listas resultantes para verificar que los datos se agregaron correctamente.

# Notas:
# - El operador `+` no modifica la lista original; crea una nueva lista combinada.
# - Puedes extender listas tantas veces como sea necesario, simplemente concatenándolas con más datos.