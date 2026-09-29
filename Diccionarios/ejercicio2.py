palabra = input("Palabra:\n\n")

frecuencia = {}

for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] = frecuencia[letra] + 1
    else:
        frecuencia[letra] = 1

print()
for letra in frecuencia:
    print(letra, ":", frecuencia[letra])
