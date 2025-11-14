import os, pygame
import random
import math
from pygame import mixer ## Submodulo para pygame para reproducir sonidos

#  Aseguramos que el directorio raiz se ejecute con los archivos del proyecto
os.chdir(os.path.dirname(os.path.abspath(__file__)))


## Inicializar pygame
pygame.init()


## Crear la pantalla
pantalla = pygame.display.set_mode((800,600))


## Titulo e iconos
pygame.display.set_caption ("Juego")
icono = pygame.image.load("nave.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')


## Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


## Variables del jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368 # Posicion X inicial (Centrado)
jugador_y = 500 # Posicion Y inicial (Centrado)
jugador_x_ = 0


## Variables enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.img.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


## Variables bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3


# Puntaje
puntaje = 0
fuente = pygame.font.Font('Sunny Spells Basic.ttf', 32)
texto_x = 10
texto_y = 10


# Texto final del juego
fuente_final = pygame.font.Font('Sunny Spells Basic.ttf', 40)


# Mostrar texto final
def texto_final():
    mi_fuente_final = fuente_final.render("Juego Finalizado", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


# Mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje:  {puntaje}" , True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion del jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))


# Funcion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))
    # Dibuja la bala desplazada desde el jugador


# Funciones para detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.poe)















se_ejecuta= True
while se_ejecuta:
    pass