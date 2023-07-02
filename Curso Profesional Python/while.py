numero = 123456789
contador = 0

# While es un ciclo que se ejecuta mientras la condicion sea verdadera
while numero >= 1: # 123456789 >= 1
    contador += 1 # contador = contador + 1
    numero = numero / 10 # 123456789 / 10 = 12345678.9
else: 
    print ("La cantidad de digitos del numero es: ", contador)
