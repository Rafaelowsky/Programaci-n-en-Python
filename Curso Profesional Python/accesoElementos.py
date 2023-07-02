elementos = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Con esto podemos sabe si es que existe una llave en nuestro diccionario

print ('z' in elementos) # False

# Ahora para poder acceder a un valor de nuestro diccionario, podemos hacerlo de la siguiente manera:

print(elementos['a']) # 1

# Si es que la llave no existe, nos va a marcar un error

# print(elementos['z']) # KeyError: 'z'

# Para evitar este error, podemos usar el método get()

print(elementos.get('z')) # None

# Podemos agregar un valor por defecto en caso no exista la llave

print(elementos.get('z', 'No se encuentra en el diccionario')) # No se encuentra en el diccionario

# Para agregar un valor por defecto en caso no exista la llave, podemos usar el método setdefault()

print(elementos.setdefault('z', {'No existe en el diccionario'}))