import sqlite3

# Conectarse a la base de datos "bd1.db"
conexion = sqlite3.connect("bd1.db")

# Solicitar al usuario que ingrese el código de un artículo
codigo = int(input("Ingrese el código de un artículo: "))

# Ejecutar una consulta para obtener la descripción y el precio del artículo con el código ingresado
cursor = conexion.execute("SELECT descripcion, precio FROM articulos WHERE codigo=?", (codigo, ))

# Obtener la primera fila del resultado
fila = cursor.fetchone()

# Verificar si se encontró un artículo con el código ingresado y mostrar la información correspondiente
if fila != None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")

# Cerrar la conexión a la base de datos
conexion.close()
