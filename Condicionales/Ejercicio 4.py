cadena = input("Ingrese una cadena de caracteres: ")
cadena = cadena.replace(" ", "").upper()
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
