numero = int(input("Número: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

if divisores == 2:
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")
