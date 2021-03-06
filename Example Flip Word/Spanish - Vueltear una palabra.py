# Limpia la consola para ver solo el programa
from os import system
system("cls")

# Le pide al usuario introducir una oracion y la longitud que debe tener la palabra para vueltearla 
oracion = input("Por favor introduce la palabra o la oracion que quieres vueltear:\n>")

longitud_palabra_vueltear = int(input("Por favor, entra la longitud que la palabra debe tener para ser vuelteada:\n>"))

# Transforma la palabra en una lista con cadenas adentro
palabras = sentence.split()

# Bucle para recorrer la lista
for palabra in palabras:

    # Comprueba que la palabra tenga la longitud indicada para ser vuelteada
    if len(palabras) >= longitud_palabra_vueltear:

        indice_palabra = palabras.index(palabra) # Guarda el indice de la palabra que cumple la condicion
        palabras[indice_palabra] = palabra[len(palabra)::-1] # Vueltea y guarda la palabra en la lista de cadenas

# Une las palabras que estaban dentro de la lista para crear la misma oracion del principio
# Pero las palabras que cumplen la condicion, seran vuelteadas y agregadas en la oracion

print(" ".join(palabras)) 