# Dibuixar formes amb transparència

Les formes que dibuixem poden tenir transparència, però el procés és una mica més complicat que el de dibuixar una figura, ja que hem de crear una superfície transparent també.

Per a fer transparències s'utilitza un color amb format (R,G,B, Alpha) on Alpha indica la quantitat d'opacitat.

Per exemple 255 és un color opac, 0 és un color completament transparent.

Aquí tenim un exemple d'un programa que crea un rectangle de color negre transparent (50 ALPHA) en mig de la pantalla de pygame.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/146146e9-e096-401c-a791-13059863677d)

```
import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
ALPHA = 50
NEGRE_TRANSPARENT = (0,0,0,ALPHA)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')

# CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
seccio_transparent = pygame.Surface((400,400),pygame.SRCALPHA)

pygame.draw.rect(seccio_transparent,NEGRE_TRANSPARENT,(0,0,400,400))

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pantalla.fill(BLANC)    

    #DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent,(100,100))

    pygame.display.update()
```


