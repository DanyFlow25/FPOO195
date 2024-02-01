def factura(sin_iva, porcentaje_iva=21):
    total = sin_iva + (sin_iva * porcentaje_iva / 100)
    return total
sin_iva = float(input("Ingrese la cantidad sin IVA: "))
porcentaje_iva_usuario = input("Ingrese el porcentaje de IVA: ")
if porcentaje_iva_usuario:
    porcentaje_iva = float(porcentaje_iva_usuario)
else:
    porcentaje_iva = 21
total = factura(sin_iva, porcentaje_iva)
print("El total de la factura es: ", total)