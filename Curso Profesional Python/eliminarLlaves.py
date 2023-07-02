diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Se pueden eliminar elementos de un diccionario con el método del y pasando como argumento el elemento que queremos eliminar
del diccionario['a'] # Eliminamos el elemento con la llave 'a'

print(diccionario) # {'b': 2, 'c': 3, 'd': 4}

# También podemos eliminar elementos con el método pop() y pasando como argumento la llave del elemento que queremos eliminar

diccionario.pop('b') # Eliminamos el elemento con la llave 'b'

# Podemos asignar el valor que eliminamos con el metodo pop() a una variable

valor = diccionario.pop('c') # Eliminamos el elemento con la llave 'c' y lo asignamos a la variable valor

print(valor) # 3

print(diccionario) # {'c': 3, 'd': 4}

# Si queremos eliminar todos los elementos de nuestro diccionario podemos usar el método clear()

diccionario.clear() # Eliminamos todos los elementos de nuestro diccionario

print(diccionario) # {}