palabra = input("Palabra: ")
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador = contador + 1

print("La palabra contiene", contador, "vocales.")
