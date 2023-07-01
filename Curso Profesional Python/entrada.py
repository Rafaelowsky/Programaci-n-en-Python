#input sirve para poder recibir datos del usuario pero este devuelve siempre un string
#lo que ingrese el usuario se va a guardar en la variable nombre
nombre = input ("Ingresa tu nombre: ")
print ("Hola " + nombre + " Bienvenido al curso de Python")

#Tambien podemos convertir el valor que nos regresa input a un entero

edad = int(input("Ingresa tu edad: "))
print(type(edad)) #<class 'int'>

#Tambien podemos convertir el valor que nos regresa input a un flotante

estatura = float(input("Ingresa tu estatura: "))
print(type(estatura)) #<class 'float'>

#Tambien podemos convertir el valor que nos regresa input a un booleano

aprobado = input("¿Autorizas (Si/No): ") == "Si"
print(type(aprobado)) #<class 'bool'>




