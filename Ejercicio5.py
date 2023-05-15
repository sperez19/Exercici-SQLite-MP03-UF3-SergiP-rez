import sqlite3

# Conectarse a la base de datos "bd1.db"
conexion = sqlite3.connect("bd1.db")

# Solicitar al usuario que ingrese un precio
precio = float(input("Ingrese un precio: "))

# Ejecutar una consulta para obtener las descripciones de los artículos con precio menor al ingresado
cursor = conexion.execute("SELECT descripcion FROM articulos WHERE precio < ?", (precio,))

# Obtener todas las filas del resultado
filas = cursor.fetchall()

# Verificar si se encontraron artículos con precio menor al ingresado y mostrar las descripciones correspondientes
if len(filas) > 0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")

# Cerrar la conexión a la base de datos
conexion.close()
