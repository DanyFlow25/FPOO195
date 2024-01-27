edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    entrada = 0
elif 4 <= edad <= 18:
    entrada = 110
else:
    entrada = 190
print("El precio de la entrada es: ", entrada)