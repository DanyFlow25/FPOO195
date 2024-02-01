import math
def area_circulo(radio):
    return math.pi * radio**2
def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura
radio_circulo = float(input("Ingrese el radio del círculo: "))
altura_cilindro = float(input("Ingrese la altura del cilindro: "))
print(f"El área del círculo es: {area_circulo(radio_circulo)}")
print(f"El volumen del cilindro es: {volumen_cilindro(radio_circulo, altura_cilindro)}")