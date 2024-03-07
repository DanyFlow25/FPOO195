import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root, gestion_usuarios):
        self.root = root
        self.gestion_usuarios = gestion_usuarios
        self.root.title("Inicio de sesión")
        
        self.label_email = tk.Label(root, text="Correo electrónico:")
        self.label_email.grid(row=0, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_password = tk.Label(root, text="Contraseña:")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        
        self.button_login = tk.Button(root, text="Iniciar sesión", command=self.validate_login)
        self.button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def validate_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Por favor, ingrese el correo y la contraseña.")
        else:
            usuario = self.gestion_usuarios.obtener_usuario_por_correo(email)
            if usuario and usuario.contraseña == password:
                self.show_message("¡Bienvenido!")
            else:
                self.show_message("Revise sus datos.")
    
    def show_message(self, message):
        messagebox.showinfo("Mensaje", message)
