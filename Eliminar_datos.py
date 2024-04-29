import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('horarios.db')
c = conn.cursor()

# Ejecutar una consulta para eliminar todos los datos de la tabla "horarios"
c.execute("DELETE FROM horarios")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se han eliminado todos los datos de la tabla 'horarios'.")