""" TIPOS DE CARACTERES """

a = 50
b = 100
c = 200
d = a+b
print(d+c)


nombre = "Nicolas"
apellido = "Diaz"
edad = 24
print("Soy "+nombre+" y tengo " + str(edad)+" años.")

""" CONDICIONALES - if"""

num = int(input("Ingrese número: "))
if num == 100:
    print("El número que ingresó es cien")
elif num > 100:
    print("El numero que ingresó no es cien, pero es mayor que cien")
else:
        print("El numero que ingresó no es cien, pero es menor que cien")



"""" COLECCIONES """
# Son cojuntos de elementos
# Lista [] -  Tupla ()  -  Diccionario {}  -

# Tupla: Se definen con (). No se puede modificar en tiempo de ejecución.   Con  [] puedo acceder al indice
tupla=(10, 20, 30, 40, 50, 60)
print(tupla[0])

# Lista: Se definen con []. Se puede modificar.    Con [] puedo acceder al indice
lista = [11, 21, 31, 41, 51, 61]
lista[2] = 3131 #Modifico
print(lista[2])
lista.append(7171) #.append para agregar, siempre agrega al final de la list
print(lista)
lista.insert(0,1011001)  #.insert en el primer n° va la poiscion, en el segundo va el valor a agregar
del lista[1]      #.delete para borrar
print(lista)



archivo=open("Temas vistos en Clase1.txt" , "w")     # W es de Write
archivo.write("Repaso general, colecciones.\nLaboratorio 'Bucle While' y Laboratorio 'Sumatoria'")
archivo.close()