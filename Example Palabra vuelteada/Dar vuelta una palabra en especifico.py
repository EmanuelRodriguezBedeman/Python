oracion = "Hola soy gardel me gusta el tinto con maní"
palabras = oracion.split()

for palabra in palabras:
    if len(palabra) >= 5:
        indice_palabra = palabras.index(palabra)
        palabras[indice_palabra] = palabra[len(palabra)::-1]
        print(" ".join(palabras))