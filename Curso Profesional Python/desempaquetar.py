#Así podemos desempaquetar elementos de una tupla

tupla = (1,2,3,4,5,6,7,8,9,10)

# * para la creación de una lista
# _ para ignorar un elemento
# *_ para ignorar varios elementos

uno, _, tres, _, *elementos_restantes = tupla

print (uno) #1
print (elementos_restantes) #[5, 6, 7, 8, 9, 10]

#Solo se permite un solo * en la desempaquetación 
