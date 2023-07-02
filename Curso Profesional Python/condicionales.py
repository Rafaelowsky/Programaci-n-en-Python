resultado = 15

# Las condicionales nos permiten evaluar si una expresión es verdadera o falsa
# dependiendo de su valor ejecutaremos cierto código

if resultado > 10 and resultado < 20:
    print ("El valor cumple con la condición")

# Si la condición no se cumple podemos ejecutar otro código
else:
    print ("El valor no cumple con la condición")

# Tambien podemos usar elif para evaluar otra condición

calificacion = 8 

if calificacion == 10:
    print ("Felicidades, tu calificación es excelente")

elif calificacion >= 6:
    print ("Felicidades, aprobaste el curso")

else:
    print ("Reprobaste el curso")