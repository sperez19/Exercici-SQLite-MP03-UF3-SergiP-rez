import sqlite3

# Conectarse a la base de datos "bd1.db"
conexion = sqlite3.connect("bd1.db")

# Insertar registros en la tabla 'articulos'
conexion.execute("INSERT INTO articulos(descripcion, precio) VALUES (?, ?)", ("naranjas", 23.50))
conexion.execute("INSERT INTO articulos(descripcion, precio) VALUES (?, ?)", ("peras", 34))
conexion.execute("INSERT INTO articulos(descripcion, precio) VALUES (?, ?)", ("bananas", 25))

# Confirmar los cambios realizados
conexion.commit()

# Cerrar la conexión a la base de datos
conexion.close()
