try:                                # con TRY se "CAPTURA EL ERROR"
    print(int("Holis"))             # Este print sin try: daría "Value Error"
except ValueError:
    print("no es una cadena de caracteres")


class NoNumError(Exception):
    pass
def sumar(num1, num2):                                # EXCepcion dentro de Def
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):             #COMPRUEBA si n1 y n2 son enteros o flotantes, y si no los puede sumar, nosotros con Raise generamos la EXCEPCION
        raise NoNumError("Se requieren dos números")
    total=num1+num2
    print(total)

try:
    sumar(1,"a")
except NoNumError:
    print("Debe colocar dos argumentos numericos")
    ## ESTE PROGRAMA DEVUELVE EL ERROR SIN PARAR EL PROGRAMA


lista=[10,20,30,40]
for i in range(0,5,1):
    try:
        print(lista[i])
    except IndexError:
        pass

alumno={"nombre":"Nicolás", "Apellido":"Díaz"}
print(alumno["dni"])

############# LABORATORIO EXCEPCIONES EN DICCIONARIO

paises = {"ar": "Argentina","es": "España","us": "Estados Unidos","fr": "Francia"}

while True:
    codigo = input("Ingrese un codigo: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El código es invalido, vuelve a intentarlo.")


num1=input("Ingrese un número:")
num2=input("Ingrese otro número:")
if not isinstance(num1, (int, float)) or not isinstance(num2, (int,float)):
    raise NoNumError("Se requieren dos números")

def calcu(num1,num2):
    suma=num1+num2
    resta=num1-num2
    div=num1/num2
    multip=num1*num2
