from os import system
from platform import system as system_os
from Warehouse import products

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
    bag = (input("Do you need any bags? (5$ each) (Yes/No)\n>")).capitalize()

    global bags_amount

    if bag == "Yes":
        bags_amount = int(input("\nHow many bags you gonna need?\n>"))

        if bags_amount == ValueError:
            print("\nError. Please introduce a number.")
        
    elif bag == "No":
        bags_amount = 0
    
    else:
        print('\nError. Answer "Yes" or "No"')


def show_price(cart):

    total = 0
    tax = 0
    bags_price = (bags_amount * 5)

    for producto in cart:

        total += products[producto]

    tax = (total + bags_price) * 0.21

    print("""
- bags({}) = {}$

Subtotal: {}$
TAX (21%)= ${:.3f}
            
-TOTAL + TAX= ${:.2f}""".format(bags_amount, bags_price, total, tax, total + tax + bags_price))
