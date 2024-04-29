import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('horarios.db')
c = conn.cursor()

# Ejecutar una consulta para agregar un campo de fecha a la tabla "horarios"
c.execute("ALTER TABLE horarios ADD COLUMN fecha DATE")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se ha agregado un campo para la fecha en la tabla 'horarios'.")