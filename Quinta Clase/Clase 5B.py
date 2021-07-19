## MANEJO DE ARCHIVOS Y CARPETAS del sist operativo
## Biblioteca OS

import os

retorno=os.listdir("c:\\clase5")                       # esto nos retorna una lista de los nombres de lo q esta dentrode la carpeta 'clase5'
print(retorno)

retorno=os.getcwd()
print(retorno)                                          # devuelve la ubicacion del directorio q toi trabajando

retorno=os.path.exists("c:\\clase5")                    # comprueba si existe el directorio(True) o sino existe(False)
print(retorno)

#os.mkdir("c:\\clase5\\prueba")                       # crear otro directorio(carpeta) con MKDIR() : make directory

#os.rmdir("c:\\clase5\\prueba")                       # para borrar directorio rmdir() - Remove directory
                                                     # rmdir SOLO BORRA carpetas vacias

#os.rename("c:\\clase5\\archivo1.txt","c:\\clase5\\a_borrar.txt")             # cambia el nombre de un archivo

#os.remove("c:\\clase5\\a_borrar.txt")                    # borra un archivo


#Biblioteca SHUTIL

import shutil
#shutil.copy("c:\\clase5\\archivo2.txt","c:\\clase5\\eliminar")        # COPIAR ARCHVOS

#shutil.move("c:\\clase5\\archivo3.txt","c:\\clase5\\eliminar")         # MOVER archivo a otro directorio

#shutil.rmtree("c:\\clase5\\eliminar")                                   # BORRA Directorio con archvos dentro