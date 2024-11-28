#El usuario introducira un numero
numero = int(input("Introdueix un numero: "))

#Comprovacion del numero puesto
if numero >= 1:
    
    suma = sum(range(1, numero + 1))
    print(f"La suma de los numeros del 1 al {numero} es: {suma}")
else:
    print("Introduzca un numero major o igual a 1, si us plau!!!")