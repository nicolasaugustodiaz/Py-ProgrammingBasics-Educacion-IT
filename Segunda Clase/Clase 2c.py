nombre="Nicolás"
edad=24

print("Soy "+nombre+" y tengo "+str(edad)+" años de edad")         # forma común de concatenar

print("Soy", nombre,"y tengo",edad,"años de edad (forma 2)", sep=" ",end="\n")     # forma 2   # sep= son los espacios # end= \n

### Place holders

print("Soy {0} y tengo {1} años de edad (forma 3 con .format)".format(nombre,edad))                 # forma 3 con .format()
                                                                                        # dentro del print con {0}{1} luego voy a pasar los valores en .format(0,1)

print(f"Soy {nombre} y tengo {edad} años de edad (forma 4 con .format)")                # forma 4 con .format()
                                                                                        # con f despues del print, toma lo q esté entre {} como variables para un .format()


### Mostrar INT con ancho mínimo de 5
print("{:05d}".format(123))

### Mostrar FLOAT con ancho mínimo de 8 ( DECIMALES, REDONDEA)
print("{:8.3f}".format(1.59999))                                                      # con .3f  le digo q muestre 3 decimales

### mostrar FLOAT sin decimales
print("Para mostrar el número {0} sin decimales y sin convertirlo a int, sería: {1:1.0f}".format(3.14654,3.14654))



print("La función .format() es %{0} {1} para concatenar int, str, float, etc. de manera sencilla.".format(100,"segura y confiable"))


### UNPACKING

tupla=(10, 20, 30)
t1,t2,t3=tupla
print(t1,t2,t3)