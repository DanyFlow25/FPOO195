class Usuario:
    def __init__(self):
        self.lista_usuarios = []

    def insertar(self, numero, nombre, edad, dinero):
        self.lista_usuarios.append({'numero': numero, 'nombre': nombre, 'edad': edad, 'dinero': dinero})

    def consultarTodos(self):
        return self.lista_usuarios

    def buscarUsuario(self, numero):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                return usuario
        return None

    def eliminar(self, numero):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                self.lista_usuarios.remove(usuario)
                return True
        return False

    def editar(self, numero, nombre, edad, dinero):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                usuario['nombre'] = nombre
                usuario['edad'] = edad
                usuario['dinero'] = dinero
                return True
        return False

    def consultarSaldo(self, numero):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                return usuario['dinero']
        return None

    def ingresarMonto(self, numero, monto):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                usuario['dinero'] += monto
                return True
        return False

    def retirarMonto(self, numero, monto):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == numero:
                if usuario['dinero'] >= monto:
                    usuario['dinero'] -= monto
                    return True
        return False

    def deposito(self, origen, monto, destino):
        for usuario in self.lista_usuarios:
            if usuario['numero'] == origen:
                for dest in self.lista_usuarios:
                    if dest['numero'] == destino:
                        if usuario['dinero'] >= monto:
                            usuario['dinero'] -= monto
                            dest['dinero'] += monto
                            return True
        return False
