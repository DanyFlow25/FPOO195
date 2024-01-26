# Solicitar al usuario el número de horas trabajadas y el coste por hora
horas = float(input("Ingrese el número de horas trabajadas: "))
coste = float(input("Ingrese el coste por hora: "))

# Calcular la paga
paga = horas * coste

# Mostrar la paga por pantalla
print("La paga correspondiente es: $",paga)
