# Desarrollar un programa de Python que cree una base de datos de SQLite llamada productos.db y una tabla de nombre productos con las siguientes columnas
# Columna Tipo de dato: id Entero nombre Texto precio Entero
# 1 Teclado 500, 2 Mouse 900, 3 Monitor 5000, 4 Parlantes 1000

import sqlite3
conn=sqlite3.connect("productos.sqlite")
cursor=conn.cursor()
cursor.execute("CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")
productos=((1,"Teclado",500),(2,"Mouse",900),(3,"Monitor",5000),(4,"Parlantes",1000))

for id, nombre, precio in productos:
    cursor.execute("INSERT INTO productos Values(?,?,?)", (id, nombre, precio))
conn.commit()

conn.close()