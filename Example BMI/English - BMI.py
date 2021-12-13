from Functions import * # Module where I created a few useful functions 

clear() # Clears the console so only the program can be seen

print("Body Mass Index Estimate")
print("----------------------------------\n") 

# Starts the program and then it calculates BMI (Body Mass Index) based on the height and the weight passed by the user.
# Then returns the BMI 
BMI = BMI_estimate() 

# From here, the program evaluates this BMI value and prints a message about it.

if BMI < 18.5:
    print('\nYour BMI is below the normal range, you have "Low Weight"\n')
    
if 18.5 <= BMI <= 24.9:
    print('Your BMI is on the normal range. Congratulations!\n')

if 25 <= BMI <= 29.9:
    print('''It's slightly above the normal range, you have "Overweight Peso"
    You shoul considerate making excercise and improving your diet.\n''')

if 30 <= BMI <= 34.9:
    print('Your BMI is above the normal range, you have "Obese Class 1"\n')

    # This function starts when this conditional is True.
    # Starts a program where ask the user a few question about abdominal obesity
    abdominal_obesity() 

if 35 <= BMI <= 39.9:
    print('''Your BMI is high above the normal range, you have "Obese Class 2"
    Please, consult as soon as posible with your trusted doctor or nutritionist.\n''')

if BMI >= 40:
    print('Your BMI is well above the normal range, you have "Obese Class 3", please consult with your trusted doctor inmediatly.\n')
