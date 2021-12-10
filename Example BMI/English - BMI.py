from Functions import * # Module where I created a few useful functions 

clear() # Clears the console so only the program can be seen

print("Body Mass Index Estimate")
print("----------------------------------\n") 

# Starts the program and then it calculates BMI (Body Mass Index) based on the height and the weight passed by the user.
# Then returns the BMI 
BMI = BMI_estimate() 

# From here, the program evaluates this BMI value and prints a message about it.

if BMI < 18.5:
    print('\nSu BMI esta por debajo del rango normal, usted tiene "Bajo Peso"\n')
    
if 18.5 <= BMI <= 24.9:
    print('Su BMI esta dentro del rango normal. ¡Felicitaciones!\n')

if 25 <= BMI <= 29.9:
    print('''Esta levemente por encima del rango normal, usted tiene "Sobre Peso"
    Debería considerar realizar ejercicio y mejorar su dieta alimentaria.\n''')

if 30 <= BMI <= 34.9:
    print('Esta por encima del rango normal, usted tiene "Obesidad Fase 1"\n')

    # This function starts when this conditional is True.
    # Starts a program where ask the user a few question about abdominal obesity
    abdominal_obesity() 

if 35 <= BMI <= 39.9:
    print('''Esta muy por encima del rango normal, usted tiene "Obesidad Fase 2"
    Por favor, consulte a la brevedad con su médico o nutricionista de confianza.\n''')

if BMI >= 40:
    print('Esta demasiado por encima del rango normal, usted es un GORDO TETÓN Por favor, vaya rajando a ver al médico. Se va a morir, culeao.\n')
