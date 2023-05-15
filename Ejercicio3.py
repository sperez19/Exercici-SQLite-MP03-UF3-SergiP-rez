import sqlite3

# Conectarse a la base de datos "bd1.db"
conexion = sqlite3.connect("bd1.db")

# Obtener un cursor para ejecutar consultas
cursor = conexion.execute("SELECT codigo, descripcion, precio FROM articulos")

# Iterar sobre cada fila del resultado y mostrarla
for fila in cursor:
    print(fila)

# Cerrar la conexión a la base de datos
conexion.close()
