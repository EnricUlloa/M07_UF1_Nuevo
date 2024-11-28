#El usuario introducira un numero
numero = int(input("Introdueix un numero: "))

#Hacemos las operaciones para hacer la tabla de multiplicacion
print(f"Taula de multiplicar del numero: {numero}")
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")