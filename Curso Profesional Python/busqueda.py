titulo_curso = 'Curso profesional de Python'

# Con el método .count() podemos contar cuantas veces aparece un caracter en un string

print(titulo_curso.count('o')) # 4
print(titulo_curso.count('Python')) # 2

# Con el método in podemos saber si un caracter o una cadena de caracteres se encuentra en una estructura

print('Python' in titulo_curso) # True
print('python' in titulo_curso) # False

# Aqui tambien podemos ocupar lower() o upper() para que no importe si es mayuscula o minuscula

# Lower() convierte todo a minuscula
print('python' in titulo_curso.lower()) # True

# Upper() convierte todo a mayuscula
print('PYTHON' in titulo_curso.upper()) # True

# Con el método startswith() podemos saber si un string comienza con un caracter o una cadena de caracteres

print(titulo_curso.startswith('C')) # True
print(titulo_curso.startswith('c')) # False

print(titulo_curso.startswith('Curso')) # True
print(titulo_curso.startswith('curso')) # False

# Con el método endswith() podemos saber si un string termina con un caracter o una cadena de caracteres

print(titulo_curso.endswith('n')) # True
print(titulo_curso.endswith('N')) # False

print(titulo_curso.endswith('Python')) # True
print(titulo_curso.endswith('python')) # False
