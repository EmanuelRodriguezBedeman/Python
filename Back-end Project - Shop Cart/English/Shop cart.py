#-------------Imports del programa------------------------

from Warehouse import productos
from Functions import *

#-------------Programa------------------------------------

clear()
print("Bienvenido al supermercado en consola")

print("-------------------------------------")

carrito = []

mostrar_contenido(productos)

print("\nPor favor, escoge que producto quieres agregar al carrito (uno a la vez):")

primer_producto = (input(">")).capitalize()

while primer_producto not in productos.keys():

    print("\nProducto no encontrado, por favor ingrese uno de los productos mostrados por pantalla.")
    primer_producto = (input(">")).capitalize()
    
carrito.append(primer_producto)

print("-------------------------------------\n")

while True:

    eleccion = (input("¿Quieres agregar otro producto? (Si/No)\n>")).capitalize()

    if eleccion == "Si":
        print("\nEsta es la lista de productos")

        mostrar_contenido(productos)

        print("\nPor favor, escoge que producto quieres agregar al carrito (uno a la vez):")
        
        otros_productos = (input("\n>")).capitalize()

        while otros_productos not in productos.keys():

            print("\nProducto no encontrado, por favor ingrese uno de los productos mostrados por pantalla.")
            otros_productos = (input(">")).capitalize()
    
        carrito.append(otros_productos)

        print("-------------------------------------\n")

    elif eleccion == "No":
        
        print("-------------------------------------\n")

        break

    else:
        print("Error. Responde con 'Si' ó 'No'")

bolsas()

print("-------------------------------------")

print("\nEste es el contenido del carrito:")

mostrar_contenido(carrito)

mostrar_precio(carrito)

print("\nGracias! Vuelva prontos!\n")