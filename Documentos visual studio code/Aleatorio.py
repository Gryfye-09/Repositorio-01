from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1, 120)
nombre = input("Dime tu nombre:")

print (f"{nombre} Adivina el numero entero entre 1 y 120")

while intentos < 9:
    estimado= int(input("Cual es tu numero?"))
    intentos += 1

    if estimado > 120 or estimado < 0:
        print("Su numero esta fuera de rango, ingrese otro numero")
    elif estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicidades {nombre} has adivinado el numero en {intentos} intentos")
        break
if estimado != numero_secreto:
    print(f"Lo siento, has utilizado todos tus intentos.")