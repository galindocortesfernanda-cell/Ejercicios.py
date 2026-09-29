#precio descuento
precio= float(input("precio: "))
descuento= float(input("descuento: "))

valor_descuento = precio* descuento / 100 
precio_final = precio - valor_descuento 


print("precio original:", precio)
print("descuento aplicado:", valor_descuento)
print("precio_final:" , precio_final)
