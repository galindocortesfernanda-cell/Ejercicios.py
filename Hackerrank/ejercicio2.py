def kangaroo(x1, v1, x2, v2):
    # Si el segundo canguro empieza más adelante y avanza más rápido (o a la misma velocidad),
    # el primer canguro nunca lo va a alcanzar.
    if v1 <= v2:
        return "NO"

    posicion1 = x1
    posicion2 = x2

    while posicion1 < posicion2:
        posicion1 = posicion1 + v1
        posicion2 = posicion2 + v2

  
        if posicion1 == posicion2:
            return "YES"

    return "NO"
