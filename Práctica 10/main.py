from gestion_usuarios import *

def menu():
    print("Seleccione una opción:")
    print("1. Agregar usuario")
    print("2. Editar usuario")
    print("3. Consultar usuarios")
    print("4. Eliminar usuario")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

def agregar_usuario(gestion_usuarios):
    gestion_usuarios.crear_usuario()

def editar_usuario(gestion_usuarios):
    id_usuario = int(input("Ingrese el ID del usuario a editar: "))
    datos_usuario = {
        "nombre": input("Ingrese el nuevo nombre del usuario: "),
        "edad": input("Ingrese la nueva edad del usuario: "),
        "direccion": input("Ingrese la nueva dirección del usuario: "),
        "contraseña": input("Ingrese la nueva contraseña del usuario: "),
        "correo": input("Ingrese el nuevo correo del usuario: ")
    }
    gestion_usuarios.editar_usuario(id_usuario, **datos_usuario)

def consultar_usuarios(gestion_usuarios):
    print("Usuarios:")
    for usuario in gestion_usuarios.consultar_usuarios():
        print(usuario)

def eliminar_usuario(gestion_usuarios):
    id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
    gestion_usuarios.eliminar_usuario(id_usuario)

if __name__ == "__main__":
    gestion_usuarios = GestionUsuarios()

    while True:
        opcion = menu()

        if opcion == "1":
            agregar_usuario(gestion_usuarios)
        elif opcion == "2":
            editar_usuario(gestion_usuarios)
        elif opcion == "3":
            consultar_usuarios(gestion_usuarios)
        elif opcion == "4":
            eliminar_usuario(gestion_usuarios)
        elif opcion == "5":
            print("Bay")
            break
        else:
            print("Opción inválida")