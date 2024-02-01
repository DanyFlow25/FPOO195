def decimal_a_binario(decimal):
    return bin(decimal)[2:]
def binario_a_decimal(binario):
    return int(binario, 2)
numero_decimal = int(input("Ingrese un número decimal: "))
print(f"El número binario equivalente es: {decimal_a_binario(numero_decimal)}")
numero_binario_input = input("Ingrese un número binario: ")
print(f"El número decimal equivalente es: {binario_a_decimal(numero_binario_input)}")