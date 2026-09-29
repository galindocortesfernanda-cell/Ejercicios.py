num1= int (input("Numero 1 :"))
num2= int(input("Numero 2 :"))

print("1. sumar ")
print("2. restar")
print("3. multiplicar")
print("4. dividir ")

operacion= int(input("Operacion: "))

if operacion ==1:
   print(num1 + num2)
elif operacion ==2:
    print(num1 - num2) 
elif operacion ==3: 
    print (num1 * num2)
elif operacion ==4:
    print (num1 / num2)

print ( "operacion " , operacion)
