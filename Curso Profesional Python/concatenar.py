#Existen varias formar para concatenar strings en Python

nombre = "Rafael"
apellido = "Zavala"

#Primera forma

nombre_completo = "Mr. " + nombre + " " + apellido + "."
print(nombre_completo)

#Segunda forma

nombre_completo = "Mr. %s %s %s." %(nombre, apellido, "Saldivar")
print(nombre_completo)

#Tercera forma

nombre_completo = "Mr. {} {}.".format(nombre, apellido)
print(nombre_completo)