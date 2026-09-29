numero = int(input("Número: "))
pares = []

for i in range(1, numero + 1):
    if i % 2 == 0:
        pares.append(str(i))

print(" ".join(pares))
