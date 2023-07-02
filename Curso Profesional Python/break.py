titulo_curso = "Curso Profesional Python"

for caracter in titulo_curso: # Itera sobre cada caracter del string titulo_curso y lo imprime
    
    if caracter == "o":
        break # Termina el ciclo for
    
    print(caracter)

for caracter in titulo_curso: # Itera sobre cada caracter del string titulo_curso y lo imprime
    
    if caracter == "r":
        continue # Salta a la siguiente iteracion
    
    print(caracter)