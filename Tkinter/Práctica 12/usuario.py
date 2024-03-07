class Usuario:
    def __init__(self, id_usuario, nombre, edad, direccion, contraseña, correo):
        self.id = id_usuario
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.contraseña = contraseña
        self.correo = correo

    def editar_usuario(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def consultar_usuario(self):
        return vars(self)
