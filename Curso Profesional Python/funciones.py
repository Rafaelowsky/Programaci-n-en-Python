# Las funciones son un conjunto de instrucciones que realizan una tarea específica
# y pueden retornar un valor o no.

# Las funciones se definen con la palabra reservada def seguida del nombre de la función
# y paréntesis. Dentro de los paréntesis se pueden definir los parámetros que recibirá la función.

def suma() : 
    numero_uno = int(input("Ingrese el primer número: "))
    numero_dos = int(input("Ingrese el segundo número: "))
    print("La suma es: ", numero_uno + numero_dos)      

suma() # Llamamos a la función suma
