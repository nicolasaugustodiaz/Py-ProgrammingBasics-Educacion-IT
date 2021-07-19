#ESCRITURA - crear un .TXT
archivo=open("prueba.txt","w")     # W es de Write
archivo.write("Hola\n")
archivo.close()                    # cierra el .txr creado

archivo=open("prueba.txt","a")     # A es de Append
archivo.write("Chau\n")
archivo.write("Adiós\n")
archivo.close()
#### LA DIFERENCIA ENTRE "W" y "A" es que W me crea el archivo de 0 y  A agrega al archivo ya creado.

lista = ["Bye\n", "Au revoir \n"]
archivo=open("prueba.txt","a")
archivo.writelines(lista)
archivo.close()


##LECTURA
archivo=open("prueba.txt","r")     # R es de Read - si no ponemos el 2do parametro, toma por defecto Read.
saludo=archivo.read()
print(saludo)
archivo.close()
##

archivo=open("prueba.txt","r")
linea=archivo.readline()          # Me trae la primera línea
print(linea)
archivo.close()
##

#Recorrer linea x linea - WHILE
archivo=open("prueba.txt","r")
linea=archivo.readline()          # Me trae la primera línea
while linea:
    print(linea)
    linea=archivo.readline()     # Lee la siguiente línea y  continúa con el ciclo While
archivo.close()
#Recorrer linea x linea - FOR
archivo=open("prueba.txt","r")
for linea in archivo.readlines():
    print(linea)
archivo.close()
##
#Contador de linea x linea - FOR
archivo=open("prueba.txt","r")
contador=1
for linea in archivo.readlines():
    print(str(contador) + ":" + linea)
    contador=contador+1
archivo.close()

archivo=open("prueba.txt","r")
for contador, linea in enumerate(archivo.readlines(),1):   #Es el mismo contdor de arriba pero con la funcion ENUMERATE de py
    print(str(contador) + ":" + linea)
archivo.close()
