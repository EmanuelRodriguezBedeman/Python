#-------------Imports del programa------------------------

from Warehouse import products
from Functions import *

#-------------Programa------------------------------------

clear()
print("Welcome to the supermarket in console")

print("-------------------------------------")

cart = []

show_content(products)

print("\nPlease, choose the product you want to add to the cart (One at the time)")

first_product = (input(">")).capitalize()

while first_product not in products.keys():
    print("\nProduct not found, please enter one of the products displayed on the window.")
    first_product = (input(">")).capitalize()
    
cart.append(first_product)

print("\n-------------------------------------\n")

while True:
    choice = (input("Do you want to add another product?(Yes/No)\n>")).capitalize()

    if choice == "Yes":
        print("\nThis is the list of the products:")

        show_content(products)

        print("\nPlease, choose which product you want to add to the cart (one at the time):")
        
        other_products = (input(">")).capitalize()
 
        while other_products not in products.keys():
            print("\nProduct not found, please enter one of the products displayed on the window.")
            other_products = (input(">")).capitalize()
    
        cart.append(other_products)

        print("-------------------------------------\n")

    elif choice == "No":
        print("-------------------------------------\n")
        break

    else:
        print('\nError. Please enter "Yes" or "No"')

bags()

print("-------------------------------------")

print("\nThis is the content of your shop cart:")

show_content(cart)

show_price(cart)

print("\nThank you very much!\n")