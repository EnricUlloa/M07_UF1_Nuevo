#El usuario introduce un primer valor
valor1 = float(input("Introdueix un primer valor: "))

#El usuario introduce un segundo valor
valor2 = float(input("Introdueix un segon valor: "))

if valor2 < valor1:
    print(f"Valor 1 es el valor mas grande: {valor1}")
elif valor1 == valor2:
    print(f"Los dos valores son iguales.")
else:
    print(f"Valor 2 es el valor mas grande: {valor2}")