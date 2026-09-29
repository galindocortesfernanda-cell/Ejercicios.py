# conversion 
segundos= int(input("ingrese la cantidad de segundos:"))

horas= segundos // 3600
minutos= (segundos % 3600) // 60
segundos_res= segundos % 60 

print(segundos , "segundos equivalen a : ")
print(horas, "hora(s)")
print(minutos,"minuto(s)")
print(segundos_res, "segundo(s)")
