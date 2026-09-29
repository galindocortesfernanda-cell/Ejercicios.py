cantidad = int(input("Cantidad de números: "))
numeros = []

print("\nNúmeros:")
for i in range(cantidad):
    num = float(input())
    numeros.append(num)

mayor = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"\nMayor: {int(mayor) if mayor.is_integer() else mayor}")
print(f"Menor: {int(menor) if menor.is_integer() else menor}")
