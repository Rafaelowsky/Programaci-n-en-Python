usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']

# Para el ciclo for, se puede usar la palabra reservada "in" para iterar sobre una lista

for usuario in usuarios:
    print(usuario)

# Para iterar sobre un rango de numeros, se puede usar la funcion range()
# range se usa para generar una lista de numeros, pero no se almacena en memoria

for i in range(50, 101, 10): # range(start, stop, step)
    print(i)
