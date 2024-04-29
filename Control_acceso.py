import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from datetime import datetime

# Función para registrar el horario de trabajo y asignar un computador
def registrar_horario():
    nombre = nombre_var.get().upper()  # Convertir el nombre a mayúsculas

    if nombre:  # Verificar que se ha seleccionado un nombre
        # Obtener la fecha y hora actuales
        fecha_hora_actual = datetime.now()

        # Formatear la fecha y hora actuales
        fecha_actual = fecha_hora_actual.strftime("%Y-%m-%d")  # Formato YYYY-MM-DD
        hora_entrada_actual = fecha_hora_actual.strftime("%I:%M %p")  # Formato 12:02 AM/PM

        # Valor por defecto para el número de computadora
        computador = '1'

        # Insertar el horario en la base de datos junto con la fecha y hora actuales
        conn = sqlite3.connect('horarios.db')
        c = conn.cursor()
        c.execute("INSERT INTO horarios (nombre, fecha, hora_entrada, computador) VALUES (?, ?, ?, ?)", (nombre, fecha_actual, hora_entrada_actual, computador))
        conn.commit()
        conn.close()

        # Obtener la ruta completa del escritorio
        escritorio = str(Path.home() / "Desktop")

        # Crear carpeta para la persona en el escritorio si no existe
        carpeta = os.path.join(escritorio, nombre)
        if not os.path.exists(carpeta):  # Verifica si la carpeta ya existe
            os.makedirs(carpeta)
        else:
            print(f"La carpeta para {nombre} ya existe en el escritorio.")

        # Mostrar mensaje de registro exitoso
        messagebox.showinfo("Registro Exitoso", f"Se ha registrado el horario para {nombre} correctamente.")
        root.destroy()  # Cerrar la ventana después de mostrar el mensaje
    else:
        # Mostrar alerta si no se ha seleccionado un nombre
        messagebox.showwarning("Alerta", "Por favor selecciona un nombre antes de registrar.")

# Lista de nombres por defecto
nombres_por_defecto = ["","nombre1","nombre2","nombre3"]  # Dejar la lista vacía para que el menú aparezca en blanco

# Crear la ventana principal
root = Tk()
root.title("Control de Acceso a la Oficina")

# Ajustar el tamaño de la ventana
root.geometry("400x200")  # Ancho x Alto

# Variable de control para el menú desplegable
nombre_var = StringVar(root)

# Crear menú desplegable para seleccionar el nombre
nombre_label = Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=10, pady=5)
nombre_menu = OptionMenu(root, nombre_var, *nombres_por_defecto)
nombre_menu.grid(row=0, column=1, padx=10, pady=5)

# Botón para registrar el horario
registrar_button = Button(root, text="Registrar Horario", command=registrar_horario)
registrar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Crear la base de datos si no existe
conn = sqlite3.connect('horarios.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS horarios
             (id INTEGER PRIMARY KEY, nombre TEXT, fecha TEXT, hora_entrada TEXT, computador TEXT)''')
conn.commit()
conn.close()

# Deshabilitar el botón de cerrar de la ventana principal
def disable_event():
    messagebox.showwarning("Alerta", "Por favor completa el registro antes de salir.")
root.protocol("WM_DELETE_WINDOW", disable_event)

# Iniciar el bucle principal de la aplicación
root.mainloop()
