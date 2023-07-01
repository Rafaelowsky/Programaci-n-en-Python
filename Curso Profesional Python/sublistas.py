lista_cursos = ['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP']

#Para acceder a una sublista se hace de la siguiente manera:
#lista[inicio:fin]

sublista = lista_cursos[0:3]
print(sublista) #['Python', 'Django', 'Flask']

#lista[inicio:fin:salto]

sublista = lista_cursos[1:9:2]
print(sublista) #['Django', 'C', 'C#', 'PHP']

#lista[inicio:] -> obtenemos una sublista desde el indice inicio hasta el final de la lista

sublista = lista_cursos[2:]
print(sublista) #['Flask', 'C', 'C++', 'C#', 'Java', 'PHP']

#lista[:fin] -> obtenemos una sublista desde el indice 0 hasta el indice fin

sublista = lista_cursos[:4]
print(sublista) #['Python', 'Django', 'Flask', 'C']

#lista[::-1] -> obtenemos una sublista invertida

sublista = lista_cursos[::-1]
print(sublista) #['PHP', 'Java', 'C#', 'C++', 'C', 'Flask', 'Django', 'Python']

#lista[:] -> obtenemos una copia de la lista

sublista = lista_cursos[:]
print(sublista) #['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP']


