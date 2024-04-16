import time
from pygame.locals import *
import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)



# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 3

# Enemics:
enemic_image = pygame.image.load('assets/nau2.png')
velocitat_enemic = 3

enemics = [pygame.Rect(10,30,32,32), pygame.Rect(50,30,32,32), pygame.Rect(90,30,32,32)]

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1

velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # controlar trets de les naus
        if event.type == KEYDOWN:
            #jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time


    # Moviment del jugador 1
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau




    # Mantenir al jugador dins de la pantalla:
    player_rect.clamp_ip(pantalla.get_rect())


    #dibuixar el fons:
    imprimir_pantalla_fons(BACKGROUND_IMAGE)

    #Actualitzar i dibuixar les bales del jugador 1:
    for bala in bales_jugador1: # bucle que recorre totes les bales
        bala.y -= velocitat_bales # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala) # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:

    # Moviment enemics
    for enemic in enemics:
        enemic.clamp_ip(pantalla.get_rect())
        pantalla.blit(enemic_image, enemic)
        enemic.x += velocitat_enemic
        if enemic.left <= 0 or enemic.right >= AMPLADA:
            for e in enemics:
                e.y += 5  # Baixem les naus 5 pixels
            velocitat_enemic = -velocitat_enemic  # Canviar direcció

    #dibuixar els jugadors:
    pantalla.blit(player_image, player_rect)


    pygame.display.update()
    clock.tick(fps)
