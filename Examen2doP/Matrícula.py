import tkinter as tk
from tkinter import messagebox
import random

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Matrícula")
        
        self.label_nombre = tk.Label(self.master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0,)
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.grid(row=0, column=1)
        
        self.label_apellido_paterno = tk.Label(self.master, text="Apellido Paterno:")
        self.label_apellido_paterno.grid(row=1, column=0,)
        self.entry_apellido_paterno = tk.Entry(self.master)
        self.entry_apellido_paterno.grid(row=1, column=1)
        
        self.label_apellido_materno = tk.Label(self.master, text="Apellido Materno:")
        self.label_apellido_materno.grid(row=2, column=0,)
        self.entry_apellido_materno = tk.Entry(self.master)
        self.entry_apellido_materno.grid(row=2, column=1)
        
        self.label_ano_nacimiento = tk.Label(self.master, text="Año de Nacimiento:")
        self.label_ano_nacimiento.grid(row=3, column=0,)
        self.entry_ano_nacimiento = tk.Entry(self.master)
        self.entry_ano_nacimiento.grid(row=3, column=1)
        
        self.label_carrera = tk.Label(self.master, text="Carrera:")
        self.label_carrera.grid(row=4, column=0,)
        self.entry_carrera = tk.Entry(self.master)
        self.entry_carrera.grid(row=4, column=1)
        
        self.button_generar = tk.Button(self.master, text="Generar Matrícula", command=self.generar_matricula)
        self.button_generar.grid(row=5, columnspan=2)
        
    def generar_matricula(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        ano_nacimiento = self.entry_ano_nacimiento.get()
        carrera = self.entry_carrera.get()
        
        if nombre and apellido_paterno and apellido_materno and ano_nacimiento and carrera:
            matricula = (
                nombre[0] +
                apellido_paterno[:2] +
                apellido_materno[:2] +
                str(ano_nacimiento)[-2:] +
                str (24) +
                carrera[:3] +
                ''.join(random.choices('0123456789', k=2))
                
            )
            messagebox.showinfo("Matrícula Generada", f"Matrícula: {matricula}")

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()

