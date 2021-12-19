import os

os.system('cls')

while True:
    print("Calculo de Índice de Masa Corporal")
    print("----------------------------------\n")
    
    peso = float(input("Ingrese su peso en Kilogramos: (Ej. 70)\n>"))
    altura = float(input("\nIngrese su altura en Metros: (Ej. 1.70)\n>"))
    
    imc = round((peso/(altura**2)),1)
    print("\nSu indice de masa corporal es:", imc)
    break

if imc < 18.5:
    print('\nSu IMC esta por debajo del rango normal, usted tiene "Bajo Peso"\n')
    
if 18.5 <= imc <= 24.9:
    print('Esta dentro del rango normal. ¡Felicitaciones!\n')

if 25 <= imc <= 29.9:
    print('''Esta levemente por encima del rango normal, usted tiene "Sobre Peso"
    Debería considerar realizar ejercicio y mejorar su dieta alimentaria.\n''')

if 30 <= imc <= 34.9:
    print('Esta por encima del rango normal, usted tiene "Obesidad Fase 1"\n')
    try:
        rta = (input("¿Usted posee miembros muy delgados y siente el abdomen muy pesado / agrandado? (Si/No)\n>")).capitalize()

        if rta == "Si": 
            print("Consulte a la brevedad con su médico de confianza.\n")

        if rta == "No":
            print("Por favor, mejore su dieta alimentaria, realice ejercicio y consulte a su nutricionista\n")

    except: 
        print("Por favor responda que Sí ó que No\n") 

if 35 <= imc <= 39.9:
    print('''Esta muy por encima del rango normal, usted tiene "Obesidad Fase 2"
    Por favor, consulte a la brevedad con su médico o nutricionista de confianza.\n''')
    
if imc >= 40:
    print('Esta demasiado por encima del rango normal. Por favor, vaya inmediatamente a ver al médico.\n')
