#Para poder crear una lista a base de un string se utiliza el metodo split
#El metodo split recibe como parametro el caracter que se va a utilizar para separar los elementos de la lista

lenguajes = "Java Python Ruby C# JavaScript"
lista = lenguajes.split(" ")

print(lista) #['Java', 'Python', 'Ruby', 'C#', 'JavaScript']

#Para unir los elementos de una lista se utiliza el metodo join
#El metodo join recibe como parametro el caracter que se va a utilizar para unir los elementos de la lista

lista_lenguajes = ["Java", "Python", "Ruby", "C#", "JavaScript"]
string = " ".join(lista_lenguajes)
print (string) #Java Python Ruby C# JavaScript


