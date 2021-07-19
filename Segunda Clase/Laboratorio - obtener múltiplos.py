#Escribir una función que, dado un número máximo,
#retorne una lista con todos los números desde 1 hasta
#dicho número que sean simultáneamente múltiplos
#de 3 y de 5 (usar la operación resto con el carácter %).

def multiplos(maximo):
    """
    Retorna una lista con números que simultáneamente son múltiplos
    de 3 y 5, hasta un valor máximo especificado.
    """
    ret = []
    for numero in range(1, maximo+1, 1):                      # Recorrer una lista con todos los números desde el 1 hasta
        if numero % 3 == 0 and numero % 5 == 0:             # Chequear que la división por 3 y 5 del número actual sea exacta.
            ret.append(numero)
    return ret
print(multiplos(100))