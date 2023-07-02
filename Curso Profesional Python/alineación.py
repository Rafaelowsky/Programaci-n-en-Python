string = 'Hola Mundo'

# Para alinear a la izquierda se usa el método ljust()

print(string.ljust(20, '-')) # Hola Mundo----------

# Para alinear a la derecha se usa el método rjust()

print(string.rjust(20, '-')) # ----------Hola Mundo

# Para centrar se usa el método center()

print(string.center(20, '-')) # -----Hola Mundo-----

# Recordad que para los métodos para alinear se necesita siempre un argumento para los espacios