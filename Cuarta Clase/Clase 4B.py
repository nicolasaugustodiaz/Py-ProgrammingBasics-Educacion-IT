### ESTRUCTURA COMúN DEL INSERT
import sqlite3
nombre=input("Ingrese nombre: ")
edad=int(input("Ingrese edad: "))
conn=sqlite3.connect("database.sqlite")
cursor=conn.cursor()
cursor.execute("INSERT INTO personas VALUES(?,?)",(nombre,edad))   # executescript me permite realizar varias consultas en una línea
conn.commit()
conn.close()