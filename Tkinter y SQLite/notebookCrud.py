from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def busUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if not usuarioBD:
        messagebox.showwarning("Nada", "Usuario no encontrado")
    else:
        Usuario.delete(1.0, tk.END)
        for usuario in usuarioBD:
            Usuario.insert(tk.END, f"ID: {usuario[0]}\nNombre: {usuario[1]}\nCorreo: {usuario[2]}\n\n")
# Creé el método para mostrar los usuarios
def buscartodos():
    usuarios = objControlador.consultarUsuarios()
    ventana_usuarios = tk.Toplevel()
    ventana_usuarios.title("Consulta de Usuarios")
    frame = ttk.Frame(ventana_usuarios)
    frame.pack(padx=10, pady=10)
    ttk.Label(frame, text="ID").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(frame, text="Nombre").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(frame, text="Correo").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(frame, text="Contraseña").grid(row=0, column=3, padx=5, pady=5)
    for i, usuario in enumerate(usuarios, start=1):
        ttk.Label(frame, text=usuario[0]).grid(row=i, column=0, padx=5, pady=5)
        ttk.Label(frame, text=usuario[1]).grid(row=i, column=1, padx=5, pady=5)
        ttk.Label(frame, text=usuario[2]).grid(row=i, column=2, padx=5, pady=5)
        ttk.Label(frame, text=usuario[3]).grid(row=i, column=3, padx=5, pady=5)
        
# Crear ventana
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

# Preparar el notebook para pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

# Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# Agregar las pestañas
panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")

# Pestaña 1: Formulario de Insert
Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Modern", 18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

# Pestaña 2: Buscar Usuario
Label(pestana2, text="Buscar Usuario", fg="blue", font=("Mono", 18)).pack()

varBus = tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar Usuario", command=busUsuario).pack()
Label(pestana2, text="Registrado:", fg="blue", font=("Mono", 14)).pack()

Usuario = tk.Text(pestana2, height=5, width=52)
Usuario.pack()

# Pestaña 3: Consultar Usuarios
Label(pestana3, text="Consultar Usuarios", fg="blue", font=("Mono", 18)).pack()
Button(pestana3, text="Consultar Usuarios", command=buscartodos).pack()
ventana.mainloop()
