#-------------Imports del programa------------------------

from Almacen import products
from Funciones import *

#-------------Programa------------------------------------

clear()
print("Bienvenido al supermercado en consola")

print("-------------------------------------")

cart = []

show_content(products)

print("\nPor favor, escoge que producto quieres agregar al carrito (uno a la vez):")

first_product = (input(">")).capitalize()

while first_product not in products.keys():

    print("\nProducto no encontrado, por favor ingrese uno de los products mostrados por pantalla.")
    first_product = (input(">")).capitalize()
    
cart.append(first_product)

print("-------------------------------------\n")

while True:

    choice = (input("¿Quieres agregar otro producto? (Si/No)\n>")).capitalize()

    if choice == "Si":
        print("\nEsta es la lista de productos")

        show_content(products)

        print("\nPor favor, escoge que producto quieres agregar al carrito (uno a la vez):")
        
        other_products = (input("\n>")).capitalize()

        while other_products not in products.keys():

            print("\nProducto no encontrado, por favor ingrese uno de los products mostrados por pantalla.")
            other_products = (input(">")).capitalize()
    
        cart.append(other_products)

        print("-------------------------------------\n")

    elif choice == "No":
        
        print("-------------------------------------\n")

        break

    else:
        print("Error. Responde con 'Si' ó 'No'")

bags()

print("-------------------------------------")

print("\nEste es el contenido del carrito:")

show_content(cart)

show_price(cart)

print("\nGracias! Vuelva prontos!\n")