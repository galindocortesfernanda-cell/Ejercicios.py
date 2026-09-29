lista = []

print("\nLista:")
for i in range(cantidad):
    num = int(input())
    lista.append(num)

mayor = lista[0]
segundo_mayor = -999999  # Valor muy pequeño inicial

for num in lista:
    if num > mayor:
        segundo_mayor = mayor
        mayor = num
    elif num > segundo_mayor and num != mayor:
        segundo_mayor = num

print(f"\n el segundo número mayor es: {segundo_mayor}")
