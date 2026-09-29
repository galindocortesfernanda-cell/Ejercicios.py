cantidad = int(input("Cantidad de números: "))
numeros = []

print("\nNúmeros:")
for i in range(cantidad):
    num = int(input())
    numeros.append(num)

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"\nPares: {pares}")
print(f"Impares: {impares}")
