#El usuario pondra dos palabras
palabra1 = input("Introdueix la primera paraula: ")
palabra2 = input("Introdueix la segona paraula: ")

if len(palabra1) >= 2 and len(palabra2) >= 2:
    
    palabranueva1 = palabra2[:2] + palabra1[2:]
    palabranueva2 = palabra1[:2] + palabra2[2:]
    
    #Mostramos los resultados
    print(f"Resultat: {palabranueva1} {palabranueva2}")
else:
    print("Introdueix 2 paraules si us plau!!!")