def getTotalX(a, b):
    
    limite_inferior = a[0]
    for numero in a:
        if numero > limite_inferior:
            limite_inferior = numero

   
    limite_superior = b[0]
    for numero in b:
        if numero < limite_superior:
            limite_superior = numero

    contador_numeros_validos = 0

    for x in range(limite_inferior, limite_superior + 1):
        
      
        es_valido = True
        for numero_a in a:
            if x % numero_a != 0:
                es_valido = False
                break  # Si falla con uno, no necesitamos seguir probando este 'x'

       
        if es_valido == True:
            for numero_b in b:
                if numero_b % x != 0:
                    es_valido = False
                    break

        if es_valido == True:
            contador_numeros_validos = contador_numeros_validos + 1

    return contador_numeros_validos
