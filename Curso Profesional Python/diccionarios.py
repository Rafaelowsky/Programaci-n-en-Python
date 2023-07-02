# Para la creación de diccionarios ocupamos llaves {} y dentro de ellas se colocan los pares de llaves:valor

elementos = {'a': 1, 'b': 2, 'c': 3, 'a': 4}

print(elementos) # {'a': 4, 'b': 2, 'c': 3}
# Como podemos ver, el diccionario no puede tener dos llaves iguales, por lo que se queda con la última llave que se le asignó

# Para poder añadir elementos a nuestro diccionario, podemos hacerlo de la siguiente manera:

elementos['nombre'] = 'Pulgas'

print(elementos) # {'a': 4, 'b': 2, 'c': 3, 'nombre': 'Pulgas'}

# Para actualizar un valor, podemos hacerlo de la siguiente manera:

elementos['nombre'] = 'Código Facilito'

print(elementos) # {'a': 4, 'b': 2, 'c': 3, 'nombre': 'Código Facilito'}

# Para poder verificar la cantidad de elementos que tiene nuestro diccionario, podemos usar la función len()

print(len(elementos)) # 4
