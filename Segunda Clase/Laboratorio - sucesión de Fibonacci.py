# Crear una función en Python que tome como
# argumento un entero que indique la cantidad de
# términos y retorne una lista como la anterior:
# la funcion almacena en la lista la sumatoria de los últimos dos numeros, lo que se conoce como "Suceción de Fibonacci"

def fib(cantidad):
    if cantidad <= 2:
        print("La cantidad debe ser mayor a 2.")
        return
    ret = [0, 1]
    while len(ret) < cantidad:                              # Añadir elementos hasta haber alcanzado la cantidad indicada.
        ret.append(ret[-1] + ret[-2])                     # Agregamos al final de la lista un elemento que es la suma de los dos anteriores (-1 y -2)
    return ret
fib(1)
print(fib(10))

########### OTRA FORMA ##############

def fib2(cantidad2):
    if cantidad2 >=2:
        l=[0,1]
        ant1=0
        ant2=1
        for cont in range(0, cantidad2-2, 1):
            num=ant1+ant2
            ant1=ant2
            ant2=num
            l.append(num)
        return(l)
    else:
        return None

if fib(25):
    print(fib(10))
else:
    print("La cantidad de términos debe ser mayor a 2")