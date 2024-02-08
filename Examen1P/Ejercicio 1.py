#Programa que visualiza los multiplos de 10 en el rango 10 - 1000.

inicio = int(input("Ingrese el número desde el cual desea iniciar a mostrar los múltiplos de 10: "))
for i in range(inicio, 1001, 10):
    print(i)