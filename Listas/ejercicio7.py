cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for i in range(cantidad):
    num = int(input())
    lista.append(num)

# Algoritmo de ordenamiento básico (Método de la Burbuja)
for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            # Intercambiar posiciones
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temporal

print("\nLista ordenada:\n")
for num in lista:
    print(num)
