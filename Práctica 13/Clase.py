import random
import string

class GeneradorContraseñas:
    def __init__(self):
        pass

    def generar(self, longitud=8, incluir_mayusculas=False, incluir_especiales=False):
        caracteres = string.ascii_lowercase
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_especiales:
            caracteres += string.punctuation

        password = ''.join(random.choice(caracteres) for _ in range(longitud))
        return password

    def comprobar_fortaleza(self, password):
        longitud = len(password)
        tiene_mayusculas = any(c.isupper() for c in password)
        tiene_especiales = any(c in string.punctuation for c in password)

        if longitud < 8:
            return "Débil"
        elif longitud == 8 and not tiene_mayusculas and not tiene_especiales:
            return "Media"
        elif longitud >= 12 and tiene_mayusculas and tiene_especiales:
            return "Fuerte"
        else:
            return "Media"