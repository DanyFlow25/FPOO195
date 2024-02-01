cantidad_base = int(input("Ingrese la cantidad de asteriscos en la base del árbol: "))
altura = 1
espacios = cantidad_base - 1

while altura <= cantidad_base:
    print(" " * espacios, end="")
    print("*" * (2 * altura - 1))
    
    altura += 1
    espacios -= 1
