import tkinter as tk
from gestion_usuarios import GestionUsuarios
from LoginTkinter import Login

def main():
    gestion_usuarios = GestionUsuarios()

    # Crear usuarios 
    while True:
        opcion = input("Agrega usuario").lower()
        if opcion == 'ok':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            nombre = input("Ingrese el nombre del usuario: ")
            edad = input("Ingrese la edad del usuario: ")
            direccion = input("Ingrese la dirección del usuario: ")
            contraseña = input("Ingrese la contraseña del usuario: ")
            correo = input("Ingrese el correo del usuario: ")
            gestion_usuarios.crear_usuario(id_usuario, nombre, edad, direccion, contraseña, correo)
        elif opcion == 'no':
            break
        else:
            print("Opción inválida")

    # Iniciar la interfaz de login
    root = tk.Tk()
    app = Login(root, gestion_usuarios)
    root.mainloop()

if __name__ == "__main__":
    main()
