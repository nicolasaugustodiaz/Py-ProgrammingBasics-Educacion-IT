## SQL con Python
                                            # SQLite es un pequeño motor de DB q viene instalado con Python

import sqlite3                           #importamos el modulo sqlite

conn=sqlite3.connect("database.sqlite")
cursor=conn.cursor()
#cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")


#personas=(("Luis", 30),("Nico", 10),("Gra", 26), ("Agus", 13))

#for nombre, edad in personas:
#    cursor.execute("INSERT INTO personas Values(?,?)", (nombre,edad))
#conn.commit()

#cursor.execute("SELECT * from personas")
#personas=cursor.fetchall()                         # el metodo fetchall() asociado al cursor, va a traer y retornar todos los registros(lo tengo q asignar a una variable)
#for nombre, edad in personas:                      # esto recorrería la tabla creada y la retorna
#    print(nombre,edad)

cursor.execute("SELECT count(*) from personas")
cant=cursor.fetchone()                              # nos devolvería la cantidad pero adentro de uan tupla ej: (4,)
print(cant[0])

try:
    cursor.execute("SELECT count(*) from tablainexistente")         # CAPTURO EL error de consulta, ya que no exite una tabla llamada "tablainexistente"
    cant=cursor.fetchone()
    print(cant[0])
except sqlite3.OperationalError:
    print("Error en la consulta")

conn.close()