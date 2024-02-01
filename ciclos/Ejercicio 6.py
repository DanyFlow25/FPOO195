saldo = 0
while True:
    operacion = input("Ingrese la operación (D para depósito, R para retiro): ")
    
    if operacion == "":
        break
    
    monto = float(input("Ingrese el monto: "))
    
    if operacion.upper() == "D":
        saldo += monto
    elif operacion.upper() == "R":
        saldo -= monto
    else:
        print("Operación no válida. Por favor, ingrese D para depósito o R para retiro.")

print(f"Saldo final en la cuenta: {saldo}")