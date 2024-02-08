#Programa con funciones y un menú que nos permita convertir temperaturas a decisión del usuario: 
# G Centígrados = (Fahremheeit - 32) x 5/9. | G Fahrenheit =(centigrados x 9/5) + 32 
# | G kelvin = centigrados + 273.15
while True:
    print("1 Fahrenheit a Celsius")
    print("2 Celsius a Fahrenheit")
    print("3 Celsius a Kelvin")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    elif opcion == "2":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == "3":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} grados Celsius son {kelvin} Kelvin.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")