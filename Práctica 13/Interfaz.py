import tkinter as tk
from tkinter import messagebox
from Clase import GeneradorContraseñas

class InterfazContraseña:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Contraseñas")
        self.master.geometry("300x250")

        self.label_longitud = tk.Label(self.master, text="Longitud:")
        self.label_longitud.grid(row=0, column=0, padx=5, pady=5)

        self.entry_longitud = tk.Entry(self.master)
        self.entry_longitud.grid(row=0, column=1, padx=5, pady=5)
        self.entry_longitud.insert(0, "8")

        self.checkbox_mayusculas_var = tk.BooleanVar()
        self.checkbox_mayusculas = tk.Checkbutton(self.master, text="Incluir mayúsculas", variable=self.checkbox_mayusculas_var)
        self.checkbox_mayusculas.grid(row=1, column=0, padx=5, pady=5)

        self.checkbox_especiales_var = tk.BooleanVar()
        self.checkbox_especiales = tk.Checkbutton(self.master, text="Incluir especiales", variable=self.checkbox_especiales_var)
        self.checkbox_especiales.grid(row=1, column=1, padx=5, pady=5)

        self.boton_generar = tk.Button(self.master, text="Generar Contraseña", command=self.generar_contraseña)
        self.boton_generar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.label_resultado = tk.Label(self.master, text="Contraseña:")
        self.label_resultado.grid(row=3, column=0, padx=5, pady=5)

        self.entry_resultado = tk.Entry(self.master, width=20)
        self.entry_resultado.grid(row=3, column=1, padx=5, pady=5)

        self.boton_comprobar = tk.Button(self.master, text="Comprobar Fortaleza", command=self.comprobar_fortaleza)
        self.boton_comprobar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generar_contraseña(self):
        longitud = int(self.entry_longitud.get())
        incluir_mayusculas = self.checkbox_mayusculas_var.get()
        incluir_especiales = self.checkbox_especiales_var.get()

        generador = GeneradorContraseñas()
        contraseña = generador.generar(longitud, incluir_mayusculas, incluir_especiales)

        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, contraseña)
        messagebox.showinfo("Contraseña Generada", f"La contraseña generada es: {contraseña}")

    def comprobar_fortaleza(self):
        contraseña = self.entry_resultado.get()
        generador = GeneradorContraseñas()
        fortaleza = generador.comprobar_fortaleza(contraseña)
        messagebox.showinfo("Fortaleza de la Contraseña", f"La contraseña es {fortaleza}.")

def main():
    root = tk.Tk()
    app = InterfazContraseña(root)
    root.mainloop()

if __name__ == "__main__":
    main()
