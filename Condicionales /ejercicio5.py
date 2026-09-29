compra = float(input("Valor de la compra: "))

if compra > 500000:
    descuento = compra * 0.10
else:
    descuento = 0

total = compra - descuento

print("Descuento: $", descuento)
print("Total a pagar: $", total) 
