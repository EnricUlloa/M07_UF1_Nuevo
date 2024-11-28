import random

#Esto escoje un numero aleatorio entre 1 y 100
adivinarnumero = random.randint(1, 100)

#Esto se encarga de contar los intentos
intents = 0

#Hacemos el bucle
while True:
    #Aqui el usuario pondra un numero
    intent = int(input("Endevina el numero (entre 1 i 100): "))
    
    intents += 1
    
    #Comprovacion del numero
    if intent < adivinarnumero:
        print("El numero es mes gran.")
    elif intent > adivinarnumero:
        print("El numero es mes petit.")
    else:
        print(f"Felicidades muchacho o muchacha! El numero era: {adivinarnumero}")
        print(f"Intentos realizados: {intents}")
        break