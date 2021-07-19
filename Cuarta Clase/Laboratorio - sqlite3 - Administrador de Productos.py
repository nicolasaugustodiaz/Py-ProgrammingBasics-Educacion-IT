import sqlite3

def pedir_entero(mensaje):
    """
    Pide un número entero a través de la consola hasta que el
    usuario ingrese un dato válido.
    """
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            pass
        else:
            # Si uso "return" adentro de un bucle no es necesario
            # usar "break", está implícito.
            return entero

# Conectarse a la base de datos (se crea automáticamente si no existe).
conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

print("Ingrese los datos del nuevo producto.")
# No uso "id" como nombre de variable porque es el nombre de una
# función incorporada de Python.
id_producto = pedir_entero("ID: ")
nombre = input("Nombre: ")
precio = input("Precio: $")

# Inserto el producto en la base de datos.
cursor.execute(
    "INSERT INTO productos VALUES (?, ?, ?)",
    (id_producto, nombre, precio)
)

# Guardo los cambios.
conn.commit()

# Imprimo todos los productos de la tabla.
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
# Uso los mismos nombres de variables que antes; no hay problema
# porque se van a reemplazar los valores.
for id_producto, nombre, precio in productos:
    print("Producto", id_producto, "-", nombre, f"- ${precio}.")

# Cerrar la conexión.
conn.close()