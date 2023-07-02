lista = [29,49,12,34,56,78,90,198]

#El metodo len() nos permite saber cuantos elementos tiene una lista

print(len(lista)) #8

#Con el metodo reverse() podemos invertir el orden de los elementos de una lista

lista.reverse()

print(lista) #[198, 90, 78, 56, 49, 34, 29, 12]

#Con el metodo sort() podemos ordenar los elementos de una lista

lista.sort()

print(lista) #[12, 29, 34, 49, 56, 78, 90, 198]

#Con el metodo count() podemos contar cuantas veces se repite un elemento en una lista

print(lista.count(29)) #1

#Ahora para poder conocer el elemento mas pequeño y el mas grande de una lista se hace de la siguiente manera:

print(lista[0])
print(lista[-1])

#Pero tambien podemos hacerlo con los metodos min() y max()

print(min(lista)) #12
print(max(lista)) #198

#Con in podemos saber si un elemento se encuentra en una lista, esto nos devuelve un valor booleano

print(29 in lista) #True
print(100 in lista) #False

#Con index() podemos saber en que indice se encuentra un elemento en una lista
#Si es que existe mas de un elemento igual al que pusismos el parametro, nos devolvera el indice del primero que encuentre

print(lista.index(29)) #0

