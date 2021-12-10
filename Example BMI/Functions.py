from os import system # For clearing the console
import platform # To see which device is the user using

# Function to clear the console based on the platform the user is using
def clear():
    if platform.system() == "Windows":
        system('cls')
    else:
        system('clear')

# This function interacts with the user asking for his weight and height
def BMI_estimate():

    # Start a loop where it asks for the user weight
    while True:

        # Tries to run the code, if a error occurs it can be grab so the program doesn't stop
        try:
            # Asks for the weight in kilograms and saves it in the variable "weight"
            weight = float(input("Enter your weight in Kilogramos: (Ej. 70)\n>"))
            break
        
        # In case the user enters a string instead of a number, this line catches the exception
        except ValueError:
            print("ERROR! Please insert a number:\n") # Message printed after getting the exception

    # Start a loop where it asks for the user height
    while True:

        # Tries to run the code, if a error occurs it can be grab so the program doesn't stop
        try: 
            # Asks for the weight in kilograms and saves it in the variable "height"
            height = float(input("\nEnter your height in meters: (Ej. 1.70)\n>"))
            break
        
        # In case the user enters a string instead of a number, this line catches the exception
        except ValueError:
            print("ERROR! Please insert a number:\n") # Message printed after getting the exception

    BMI = round((weight/(height**2)),1) # Calculates the BMI ( weight divided by height squared )
    print("\nYour Body Mass Index is:", BMI) # Prints a message in the console with the value of the BMI
    return BMI

# This function will be used if the BMI is in range [30 - 34.9] to check if the user have abdominal obesity or not
def abdominal_obesity():
    
    # Makes a question to the user and saves it into the variable "answer"
    answer = (input("Do you have thin limbs and feel the abdomen very heavy? (Yes/No).\n>")).capitalize()

    # If the user answer was Yes, this conditional becomes true and the code inside is trigger
    if answer == "Yes": 
        print("Consult your trusted doctor as soon as possible.\n") # Prints a message in the console

    # If the user answer was NO, this conditional becomes true and the code inside is trigger
    elif answer == "No":
        print("Please, improve your diet, make exercise and consult your nutricionist.\n") # Prints a message in the console

    # In case the user didn't answer the question the way it was asked:
    else: 
        print("Please answer Yes or Not.\n") 