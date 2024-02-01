# Capturar la cantidad de payasos y muñecas vendidos
cantidad_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

# Definir el peso de cada payaso y muñeca
peso_payaso = 112  
peso_muneca = 75   

# Calcular el peso total del paquete
peso_total = (cantidad_payasos * peso_payaso) + (cantidad_munecas * peso_muneca)

# Mostrar el resultado
print ("El peso total del paquete es: ", peso_total , "g")