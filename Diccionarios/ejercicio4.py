frase = input("Frase:\n\n")

palabras = frase.split()
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1
    else:
        conteo[palabra] = 1

print()
for palabra in conteo:
    print(palabra, ":", conteo[palabra])
