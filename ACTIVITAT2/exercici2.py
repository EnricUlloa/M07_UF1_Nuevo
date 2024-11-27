#Se le pide al usuario poner una cantidad en euros
valor = float(input("Introdueix un valor en euros: "))

#Se le pide al usuario poner el porcentaje de IVA
while True:
    IVA = int(input("Introdueix el porcentatge d'IVA: "))
    if IVA in [4, 10, 21]:
        break
    else:
        print("IVA incorrecte. Posi un percentatge dels 3 vàlids.")
        
#Calculo para saber el precio final con el IVA incluido
final = float(valor * (1 + (IVA / 100)))

#Mostramos todos los resultados que ha puesto el usuario
print(f"Valor introducido: {valor:.2f} euros.")
print(f"Porcentaje introducido: {IVA}%.")
print(f"Precio final con IVA incluido: {final:.2f} euros.")
