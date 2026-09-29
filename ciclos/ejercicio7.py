cantidad = int(input("Cantidad: "))

positivos = 0
negativos = 0
ceros = 0

print("Números:")
for i in range(cantidad):
    num = float(input())
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
