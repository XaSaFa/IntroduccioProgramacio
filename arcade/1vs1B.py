import random
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
velocitat_nau = 1


# Jugador 2:
player_image2 = pygame.image.load('assets/nau2.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 150))
velocitat_nau2 = 1


# vides:
vides1 = 3
vides2 = 3
vida_image = pygame.image.load('assets/cor.png')
vida1_jugador1 = vida_image.get_rect(midbottom=(300,180))
vida2_jugador1 = vida_image.get_rect(midbottom=(280,180))
vida3_jugador1 = vida_image.get_rect(midbottom=(260,180))
vida1_jugador2 = vida_image.get_rect(midbottom=(20,20))
vida2_jugador2 = vida_image.get_rect(midbottom=(40,20))
vida3_jugador2 = vida_image.get_rect(midbottom=(60,20))

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA),pygame.FULLSCREEN)
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def imprimir_pantalla_random(guanyador):
    num_cercles = random.randint(30,50)
    font2 = pygame.font.SysFont(None, 30)
    img2 = font2.render(guanyador, True, (0, 0, 0))

    for i in range(num_cercles):
        centre_X = random.randint(10,310)
        centre_Y = random.randint(10, 190)
        radi = random.randint(10,200)
        color_R = random.randint(0,255)
        color_G = random.randint(0,255)
        color_B = random.randint(0,255)
        pygame.draw.circle(pantalla, (color_R,color_G,color_B),(centre_X,centre_Y),radi)
        pantalla.blit(img2, (10, 100))
        time.sleep(0.1)
        pygame.display.update()
jugar = True

while jugar:
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
            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                temps_ultima_bala_jugador2 = current_time

    # Moviment del jugador 1
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau
    # Moviment del jugador 2
    if keys[K_LEFT]:
        player_rect2.x -= velocitat_nau2
    if keys[K_RIGHT]:
        player_rect2.x += velocitat_nau2



    # Mantenir al jugador dins de la pantalla:
    player_rect.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())

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
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala
            vides2 -= 1
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    # Actualitzar i dibuixar les bales del jugador 2:
    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > ALTURA:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bala_imatge, bala)
        # Detectar col·lisions jugador 1:
        if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 2!")
            bales_jugador2.remove(bala)  # eliminem la bala
            vides1 = vides1 - 1
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    #dibuixar els jugadors:
    pantalla.blit(player_image, player_rect)
    pantalla.blit(player_image2, player_rect2)

    #dibuixar vides:
    if vides1 >= 1:
        pantalla.blit(vida_image, vida1_jugador1)
    if vides1 >= 2:
        pantalla.blit(vida_image, vida2_jugador1)
    if vides1 == 3:
        pantalla.blit(vida_image, vida3_jugador1)
    #dibuixar vides:
    if vides2 >= 1:
        pantalla.blit(vida_image, vida1_jugador2)
    if vides2 >= 2:
        pantalla.blit(vida_image, vida2_jugador2)
    if vides2 == 3:
        pantalla.blit(vida_image, vida3_jugador2)
    if vides1 <= 0 or vides2 <= 0:
        if vides1 <= 0:
            guanyador = "Guanya el jugador 1!"
        else:
            guanyador = "Guanya el jugador 2!"
        imprimir_pantalla_random(guanyador)
        jugar = False
    pygame.display.update()
    clock.tick(fps)
