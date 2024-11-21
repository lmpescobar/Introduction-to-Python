# Transcripción de video introductorio: "Variables and Types"

### 1. **Variables y Tipos** (00:00 - 00:12)
¡Bien hecho y bienvenido de nuevo! Está claro que Python es una excelente calculadora. Sin embargo, si deseas realizar cálculos más complejos, querrás "guardar" valores mientras trabajas en tu código.

---

### 2. **Variable** (00:12 - 00:50)
Puedes hacerlo definiendo una variable con un nombre específico y sensible a mayúsculas y minúsculas. Una vez que creas (o declaras) una variable, puedes llamar su valor más tarde simplemente escribiendo su nombre.

Por ejemplo, supongamos que mides tu altura y peso en unidades métricas: tienes una altura de 1.79 metros y pesas 68.7 kilogramos. Puedes asignar estos valores a dos variables llamadas `height` (altura) y `weight` (peso) utilizando el signo igual:

```python
height = 1.79
weight = 68.7
```

Si ahora escribes el nombre de la variable `height`, Python buscará ese nombre, recuperará su valor y lo mostrará.

---

### 3. **Calcular el Índice de Masa Corporal (BMI)** (00:50 - 01:37)
Ahora calculemos el Índice de Masa Corporal (BMI, por sus siglas en inglés), que se calcula como sigue:

\[
\text{BMI} = \frac{\text{weight}}{\text{height}^2}
\]

Puedes hacerlo utilizando los valores reales o usando las variables `height` y `weight`, como en este ejemplo. Cada vez que escribes el nombre de una variable, le estás pidiendo a Python que lo sustituya por el valor almacenado en ella.

Por ejemplo:
```python
bmi = weight / height ** 2
print(bmi)
```

El valor calculado se almacena en una nueva variable llamada `bmi`. Esto hace que el código sea más reproducible y fácil de modificar.

---

### 4-5. **Reproducibilidad** (01:37 - 02:02)
Supongamos que el código para crear las variables `height`, `weight` y `bmi` está en un script. Si necesitas recalcular el BMI para otro peso, simplemente puedes cambiar la declaración de la variable `weight` y ejecutar el script nuevamente:

```python
weight = 74.2  # Nuevo peso
bmi = weight / height ** 2
print(bmi)
```

El valor de `bmi` cambiará automáticamente porque `weight` tiene un nuevo valor.

---

### 6. **Tipos de datos en Python** (02:02 - 02:34)
En Python, los números tienen un tipo específico. Puedes verificar el tipo de un valor utilizando la función `type()`. Por ejemplo, para nuestro valor de `bmi`:

```python
print(type(bmi))  # Resultado: <class 'float'>
```

Un `float` es la forma en que Python representa un número real, que puede tener una parte entera y una parte decimal. También existe el tipo `int` para números enteros.

---

### 7. **Tipos de datos adicionales** (02:34 - 03:12)
Python incluye muchos otros tipos de datos. Los más comunes son las cadenas (strings) y los booleanos (booleans).

- Una **cadena** es la forma de representar texto en Python. Puedes usar comillas dobles o simples para crearlas:
  ```python
  x = "body mass index"
  y = 'this works too'
  print(type(x))  # Resultado: <class 'str'>
  ```

- Un **booleano** es un tipo que puede ser `True` o `False`, como "Sí" o "No" en lenguaje cotidiano:
  ```python
  z = True
  print(type(z))  # Resultado: <class 'bool'>
  ```

Estos tipos serán muy útiles más adelante, por ejemplo, al filtrar datos.

---

### 8. **Comportamiento basado en tipos** (03:12 - 03:48)
El comportamiento del código en Python depende del tipo de datos con el que trabajes. Observa estos ejemplos:

- Sumar dos enteros:
  ```python
  print(2 + 3)  # Resultado: 5
  ```

- Sumar dos cadenas:
  ```python
  print('ab' + 'cd')  # Resultado: 'abcd'
  ```

El operador `+` se comporta de manera diferente dependiendo de los tipos de datos. Esto es un principio general en Python.

---

### 9. **¡A practicar!** (03:48 - 04:00)
¡Es hora de que empieces a escribir código! En los ejercicios que siguen, crearás tus primeras variables y experimentarás con algunos de los tipos de datos de Python. ¡Nos vemos en el próximo video, donde aprenderás todo sobre las listas! 😊