#Tuplas: Son inmutables, no se pueden modificar
#Pueden contener cualquier tipo de dato
#        0,1,2,    3,    4,    5,      6,       7
tupla = (1,2,3, "Hola", 3.14, True, [1,2,3], (1,2,3))

print(tupla[0]) #1
print(tupla[4]) #3.14
print(tupla[7]) #[1, 2, 3]

#Podemos generar una lista a partir de una tupla

cursos = ("Python", "Django", "Java")

lista_cursos = list(cursos)

print(lista_cursos) #['Python', 'Django', 'Java']

#Así como tambien podemos generar una tupla a partir de una lista

niveles = ["Basico", "Intermedio", "Avanzado"]

tupla_niveles = tuple(niveles)

print(tupla_niveles) #('Basico', 'Intermedio', 'Avanzado')

#Así podemos desempaquetar elementos de una tupla

tupla = (1,2,3,4,5,6,7,8,9,10)

# * para la creación de una lista
# _ para ignorar un elemento
# *_ para ignorar varios elementos
uno, _, tres, _, *elementos_restantes = tupla

print (uno) #1
print (elementos_restantes) #[5, 6, 7, 8, 9, 10]

#Solo se permite un solo * en la desempaquetación 
