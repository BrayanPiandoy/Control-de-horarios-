import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('horarios.db')

# Crear un cursor para ejecutar consultas
c = conn.cursor()

# Ejecutar una consulta (por ejemplo, seleccionar todos los registros de la tabla "horarios")
c.execute("SELECT * FROM horarios")

# Obtener los resultados de la consulta
filas = c.fetchall()
for fila in filas:
    print(fila)

# Cerrar la conexión cuando hayas terminado
conn.close()
