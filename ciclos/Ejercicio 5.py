frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
