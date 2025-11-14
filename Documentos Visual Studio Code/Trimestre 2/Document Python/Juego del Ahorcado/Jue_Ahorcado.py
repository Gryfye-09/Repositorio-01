from random import choice


palabras = ["sol", "luna", "mar", "montaña", "flor", "viento", "río", "estrella", "nube", "fuego", "tierra", "nieve", "bosque", "trueno", "cielo"]

letras_correctas = []
letras_incorrectas = []

intentos = 6

juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:

        letra_elegida = input("Elige una letra").lower()

        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True

        else:
            print("La letra no es correcta")

    return letra_elegida


def mostrar_tablero(palabra_elegida):
    tablero = ""

    for letra in palabra_elegida:
        if letra in letras_correctas:
            tablero += letra + " "
        else:
            tablero += "_ "

    print("\nPalabra:", tablero)
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
    print(f"Vidas restantes: {intentos}\n")


def comprobar_letra(letra, palabra):
    global intentos

    if letra in palabra:
       
        letras_correctas.append(letra)
        print(f" ¡Bien hecho! La letra '{letra}' está en la palabra.\n")
    else:
    
        letras_incorrectas.append(letra)
        intentos -= 1
        print(f" La letra '{letra}' NO está en la palabra. Pierdes una vida.\n")


def comprobar_ganar(palabra):

    for letra in palabra:
        if letra not in letras_correctas:
            return False
    return True


def jugar():
    
    global intentos, juego_terminado, letras_correctas, letras_incorrectas

    palabra_secreta = elegir_palabra(palabras)

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra secreta. Tienes 6 vidas.\n")

   
    while not juego_terminado:
       
        mostrar_tablero(palabra_secreta)

        letra = pedir_letra()

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya intentaste esa letra. Elige otra.\n")
            continue 

        comprobar_letra(letra, palabra_secreta)

        if comprobar_ganar(palabra_secreta):
            mostrar_tablero(palabra_secreta)
            print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            juego_terminado = True

        elif intentos == 0:
            print("Te quedaste sin vidas. La palabra era:", palabra_secreta)
            juego_terminado = True


jugar() 