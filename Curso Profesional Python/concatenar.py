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

nombre_completo = "Mr. {primer_apellido} {segundo_apellido} {nombre}.".format(
    nombre=nombre, 
    primer_apellido=apellido, 
    segundo_apellido="Saldivar")

print(nombre_completo)

#Cuarta forma 
#Con los f-strings podemos hacer operaciones dentro de las llaves y concatenar strings

nombre_completo = f"Mr. {nombre} {apellido} {2 * 100}."


print(nombre_completo)