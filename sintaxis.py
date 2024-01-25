
# Practica2: Sintaxis Python

#1. Comentarios

#Soy un comentario de una línea

'''soy un 
comentarios 
de 
varias líneas
'''
"""
#2 cadenas 

print ('Soy una cadena')
print("Soy otra cadena")

a= 'mi banda favorita es'
b= "grupo marrano"
print (a+b)
print (a,b)

#contar los caracteres 
print (len(a))

#
print(b[2:5])
print(b[:5])
print(b[2:])
"""
"""
#3. Variables

x = int(5)
y = str("3")
z = float(3.2)

print(x)
print(y)
print(z)

import random

numero = random.randrange(1,15)
print(numero)
"""
"""
#4. Solicitud de datos

var1 = input("introduce cualquier dato")
var2= str(input("introduce cadenas"))
var3=int(input("introduce solo enteros"))
var4=float(input("introdice numeros decimales"))

print(var1, var2, var3, var4)
"""
"""
#5. Booleans, operadores de comparación y 

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 >= 9)
print(10 != 9)
print(10 <= 9)
"""

x=1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not (x < 5 and x < 10))

#Para operaciones binarias
print(x < 5 & x < 10)
print(x < 5 | x < 10)
print(not (x < 5 & x < 10))