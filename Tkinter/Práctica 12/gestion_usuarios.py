from usuario import Usuario

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, id_usuario, nombre, edad, direccion, contraseña, correo):
        nuevo_usuario = Usuario(id_usuario, nombre, edad, direccion, contraseña, correo)
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

    def obtener_usuario_por_correo(self, correo):
        for usuario in self.usuarios:
            if usuario.correo == correo:
                return usuario
        return None

    def __buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
