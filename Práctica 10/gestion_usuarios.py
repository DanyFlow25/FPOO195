from usuario import *

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self):
        datos_usuario = {
            "id_usuario": int(input("Ingrese el ID del usuario: ")),
            "nombre": input("Ingrese el nombre del usuario: "),
            "edad": input("Ingrese la edad del usuario: "),
            "direccion": input("Ingrese la dirección del usuario: "),
            "contraseña": input("Ingrese la contraseña del usuario: "),
            "correo": input("Ingrese el correo del usuario: ")
        }
        nuevo_usuario = Usuario(**datos_usuario)
        self.usuarios.append(nuevo_usuario)

    def editar_usuario(self, id_usuario, **kwargs):
        usuario = self.__buscar_usuario(id_usuario)
        if usuario:
            usuario.editar_usuario(**kwargs)
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self, id_usuario):
        usuario = self.__buscar_usuario(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
        else:
            print("Usuario no encontrado.")

    def consultar_usuarios(self):
        return [usuario.consultar_usuario() for usuario in self.usuarios]

    def __buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None