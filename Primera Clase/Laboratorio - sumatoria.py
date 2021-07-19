# Ejercicio: Crear un bucle que almacene en una variable la suma de todos los elementos numéricos de una
# lista, con excepción del último.

numeros=[1,2,3,4,5,6]
resultado = 0
for i,numero in enumerate(numeros):
    if i == len(numeros)-1:          #con este if evito sumar el último n° de la lista
        break
    resultado+=numero
print(resultado)