def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Contador para las manzanas que caen en la casa
    manzanas_en_casa = 0
    
    for manzana in apples:
        posicion_manzana = a + manzana
        # Si la posición está entre inicio (s) y fin (t) de la casa
        if posicion_manzana >= s and posicion_manzana <= t:
            manzanas_en_casa = manzanas_en_casa + 1

    naranjas_en_casa = 0
    
  
    for naranja in oranges:
        posicion_naranja = b + naranja
        # Si la posición está entre inicio (s) y fin (t) de la casa
        if posicion_naranja >= s and posicion_naranja <= t:
            naranjas_en_casa = naranjas_en_casa + 1

    print(manzanas_en_casa)
    print(naranjas_en_casa)
