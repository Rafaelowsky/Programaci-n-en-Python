lista_cursos = ['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP']
lista_cursos2 = ['JavaScript', 'Angular', 'React', 'VueJS']

#Para agregar elementos a una lista se hace de la siguiente manera:

lista_cursos.append('Ruby')
print(lista_cursos) #['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP', 'Ruby']

#Para agregar varios elementos a una lista se hace de la siguiente manera:

lista_cursos.extend(lista_cursos2)
#['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP', 'Ruby', 'JavaScript', 'Angular', 'React', 'VueJS']

#Para agregar un elemento en una posición especifica se hace de la siguiente manera:

lista_cursos.insert(5,'Go')
#['Python', 'Django', 'Flask', 'C', 'C++', 'Go', 'C#', 'Java', 'PHP', 'Ruby', 'JavaScript', 'Angular', 'React', 'VueJS']

#Para eliminar un elemento de una lista se hace de la siguiente manera:

lista_cursos.remove('PHP')

#Para eliminar el ultimo elemento de una lista se hace de la siguiente manera:

lista_cursos.pop()
del lista_cursos[-1]

#Para eliminar un elemento de una lista por su indice se hace de la siguiente manera:

del lista_cursos[4]
lista_cursos.pop(3)
#['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'Ruby', 'JavaScript', 'Angular', 'React', 'VueJS']
#La diferencia entre del y pop es que pop devuelve el elemento eliminado


#Para eliminar todos los elementos de una lista se hace de la siguiente manera:

lista_cursos.clear()
del lista_cursos[:]