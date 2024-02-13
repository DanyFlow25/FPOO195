import random

def lista_aleatoria():
    return [random.randint(10, 20) for _ in range(30)]

lista = lista_aleatoria()

print(lista)

def repetidos(lista):
    return {numero : lista.count(numero) for numero in set(lista)}

def eliminar_repetidos(lista):
    return list(set(lista))

def reemplazar_cero(lista):
    for nume in set(lista):
        while lista.count(nume) > 1:
            lista[lista.index(nume)] = 0
    return lista


while True:
    opcion = input("\n1. Contar número repetidos\n2. Eliminar número repetidos\n3. Reemplazar repetidos con 0\n4. Salir\nElija una opción: ")
    
    if opcion == '1':
        print("Conteo de números repetidos:", repetidos(lista))
    elif opcion == '2':
        print("Lista sin números repetidos:", eliminar_repetidos(lista))
    elif opcion == '3':
        print("Lista con números repetidos reemplazados por 0:", reemplazar_cero(lista))
    elif opcion == '4':
        print("Adiós.")
        break
    else:
        print("Opción no válida.")
