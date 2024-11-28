#Se le pide al usuario que ponga entre 1 y 3 palabras
texto = input("Introduiex entre 1 i 3 paraules: ")

palabras = texto.split()

#Contador de palabras
if 1 <= len(palabras) <= 3:
    
    for palabra in palabras:
        longitud = len(palabra)
        primeraletra = palabra[0]
        ultimaletra = palabra[-1]
        
        #Mostrar resultados
        print(f"Palabra: {palabra}")
        print(f"Cantidad de caracteres: {longitud}")
        print(f"Primer caracter: {primeraletra}")
        print(f"Ultimo caracter: {ultimaletra}")
        print()
else:
    print("Introdueixi entre 1 i 3 paraules si us plau!")