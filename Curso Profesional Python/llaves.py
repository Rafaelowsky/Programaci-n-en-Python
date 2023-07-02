diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Podemos obtener las llaves de nuestro diccionario con el método keys()

print(diccionario.keys()) # dict_keys(['a', 'b', 'c', 'd']) 

# Tambien podemos obtener los valores de nuestro diccionario con el método values()

print(diccionario.values()) # dict_values([1, 2, 3, 4])

# Ya por ultimo podemos obtener los elementos de nuestro diccionario con el método items()

print(diccionario.items()) # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# Como extra podemos transformar nuestro diccionario en una tupla

print(tuple(diccionario.items())) # (('a', 1), ('b', 2), ('c', 3), ('d', 4))



