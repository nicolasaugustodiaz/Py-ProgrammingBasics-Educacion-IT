## SCRIPTING y Cadenas de caracteres

s="cadena de caracteres"
print(s[0:6])                    ## esta tecnica es slising  ( "fetear" )
#print(s[:6])            --> es lo mismo q el de arriba
#print(s[10:])

## COMPRUEBA CON startswith() si la cadena arranca con()  y con endswith() si finaliza con()
if s.startswith("cadena"):
    print("si, empeiza con 'cadena'")

if s.endswith("caracteres"):
    print("si, termina con 'caracteres'")


## STRIP() borra del principio y del final: los espacion y los new line(\n)

opcion=input("Continuar?: ")
if opcion.strip()=="si":
    print("Usted eligió continuar")

## REEMPLAZAR ( como los string no son manipulables, se debe almacenar en otra variable)

s2=s.replace("cadena de caracteres","string")
print(s2)

## REEMPLAZAR y poner en una lista - SPLIT()

milista=s.split()
print(milista)