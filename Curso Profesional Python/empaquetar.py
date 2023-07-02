#Para empaquetar se usa la funcion zip
lista = [1,2,3,4,5,6,7,8,9,10]

dupla = (1,2,3,4,5,6,7,8,9,10)

#Cuando hay mas de un elemento en la lista o tupla con el que no se pueda empaquetar, se ignora
lista_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

dupla_2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

lista_3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

#Este es otro ejemplo de como se ignora un elemento
dupla_3 = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200)

resultado = zip (lista,dupla,lista_2,dupla_2)
resultado = tuple (resultado)
print(resultado) 