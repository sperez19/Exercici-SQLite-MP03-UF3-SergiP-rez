import sqlite3

# Conectarse a la base de datos "bd1.db"
conexion = sqlite3.connect("bd1.db")

try:
    # Crear la tabla 'articulos' si no existe
    conexion.execute("""CREATE TABLE IF NOT EXISTS articulos (
                              codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                              descripcion TEXT,
                              precio REAL
                        )""")
    print("Se creó la tabla 'articulos'")
except sqlite3.OperationalError:
    # La tabla 'articulos' ya existe en la base de datos
    print("La tabla 'articulos' ya existe")

# Cerrar la conexión a la base de datos
conexion.close()
