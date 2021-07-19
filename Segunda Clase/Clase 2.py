
def suma1(n1,n2):
    total=n1+n2
    return total
resultado = suma1(100,200)
print("El resultado de la suma1 es: " +str(resultado))

#################################################################
def sumar2(num1=10,num2=20):
    total=num2+num2
    return total
print("El resultado de la suma2 es: "+ str(sumar2(num2=30)))


############ TXT TEMAS VISTOS EN CLASE
archivo=open("Temas vistos en Clase2.txt","w")     # W es de Write
archivo.write("Crear, abrir leer y editar archivos .txt - open(), read(), write(), readline().\nPlace Holders, .format() y Unpacking."
               "\nLaboratorio 'Obtener Múltiplos y Laboratorio 'Sucesión de Fibonacci.'")
archivo.close()
