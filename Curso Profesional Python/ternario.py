calificacion = 10

# Las condicionales tambien las podemos ocupar directamente en una declaracion de variable
# así nos ahorraremos algunas lineas de código

color = "Verde" if calificacion >= 7 else "Rojo"
print (color)

# En este caso si la calificación es mayor o igual a 7 el color será verde, de lo contrario será rojo
# Esto es lo mismo que hacer lo siguiente:

if calificacion >= 7:
    color = "Verde"
else:
    color = "Rojo"

print (color)

# Tambien podemos ocupar or en lugar de and para evaluar dos condiciones

listado = [] # False
nombre = 'Cody' # True

"""
if listado:
    variable = listado
else:
    variable = nombre
"""

variable = listado or nombre
print (variable) # Cody