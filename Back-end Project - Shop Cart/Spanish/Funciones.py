from os import system
from platform import system as system_os
from Almacen import products

def clear():
    if system_os() == "Windows":
        system('cls')

    else:
        system('clear')

def show_content(container):

    for product in container:

        if type(container) == dict:
            print("\n -{}, ${}".format(product, container[product]))
        
        elif type(container) == list:
            print("\n -{} ${}".format(product, products[product]))
        
        
def bags():
    global bags_amount

    while True:
        bag = (input("¿Necesitas bolsas? 5$ c/u (Si/No)\n>")).capitalize()

        if bag == "Si":

            while True:
            
                try:
                    bags_amount = int(input("\n¿Cuantas bolsas vas a necesitar?\n>"))

                except ValueError:
                    print("\nError. Por favor, introduce un numero.")

                else:
                    return bags_amount
            
        elif bag == "No":
            bags_amount = 0
            break
        
        else:
            print('\nError. Por favor, responde "Si" o "No"')


def show_price(cart):

    total = 0
    tax = 0
    bags_price = (bags_amount * 5)

    for product in cart:
        total += products[product]

    tax = (total + bags_price) * 0.21

    print("""
- Boslas({}) = {}$

Subtotal: {}$
TAX (21%)= ${:.3f}
            
-TOTAL + TAX= ${:.2f}""".format(bags_amount, bags_price, total, tax, total + tax + bags_price))