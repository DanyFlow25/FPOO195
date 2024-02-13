def capturar_numeros():
    n = int(input("Ingrese la cantidad de números que desea ingresar en la tupla: "))
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(n)]
    return tuple(numeros)

def sumatoria(tupla):
    return sum(tupla)

def numero_mayor(tupla):
    return max(tupla)

def numero_menor(tupla):
    return min(tupla)

def promedio(tupla):
    return sum(tupla) / len(tupla)

def moda(tupla):
    conteo = {}
    for num in tupla:
        conteo[num] = conteo.get(num, 0) + 1
    moda = max(conteo, key=conteo.get)
    return moda

def rango(tupla):
    return max(tupla) - min(tupla)

def menu():
    print("Selecciona una opción:")
    print("1. Sumatoria de los elementos de la lista")
    print("2. Número mayor de la lista")
    print("3. Número menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")
    print("7. Salir")

tupla_numeros = capturar_numeros()

while True:
    menu()
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("La sumatoria de los elementos de la lista es:", sumatoria(tupla_numeros))
    elif opcion == 2:
        print("El número mayor de la lista es:", numero_mayor(tupla_numeros))
    elif opcion == 3:
        print("El número menor de la lista es:", numero_menor(tupla_numeros))
    elif opcion == 4:
        print("El promedio de la lista es:", promedio(tupla_numeros))
    elif opcion == 5:
        print("La moda de la lista es:", moda(tupla_numeros))
    elif opcion == 6:
        print("El rango de la lista es:", rango(tupla_numeros))
    elif opcion == 7:
        print("BAY")
        break
    else:
        print("Opción no válida")
