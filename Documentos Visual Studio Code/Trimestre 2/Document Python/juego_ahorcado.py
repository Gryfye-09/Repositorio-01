from random import choice

palabras = ["computador", "celular", "teclado", "pantalla"]
letras_correctas = []
letras_incorrectas = []

intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:

        letra_elegida = input("Elige una letra")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True

        else:
            print("La letra no es correcta")
    return letra_elegida

def nuevo_tablero(palabra_elegida):


def chequear_letra():


def perder():


def ganar():