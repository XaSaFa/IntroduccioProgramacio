# Text a Pygame

Pygame no pot imprimir text per pantalla directament, el que fa es crear una font i generar una imatge amb el text.

## Fonts a Pygame:

Podem utilitzar qualsevol font instalada al sistema o None per utilitzar una font per defecte.

Per conèixer les fonts instal·lades podem imprimirles així:

```
import pygame

fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)
```

## Escriure un text per pantalla:

Anem a fer un programa que digui "Hello World!" amb lletres de color vermell en mig de la pantalla, això ho fem així:

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
pygame.display.set_caption('Text')

#FONT I TEXT de tamany 64
font = pygame.font.SysFont(None,64)
img = font.render("Hello World!", True, VERMELL)


while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pantalla.fill(BLANC)
    #dibuixem el text a la posició 200,200
    pantalla.blit(img, (200, 200))


    pygame.display.update()
```

Podem crear tantes fonts diferents al nostre programa com vulguem:

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
pygame.display.set_caption('Text')

#FONT I TEXT de tamany 64
font = pygame.font.SysFont(None,64)
img = font.render("Hello World!", True, VERMELL)

font2 = pygame.font.SysFont("freemono",50)
img2 = font2.render("¡Hola Mundo!", True, NEGRE)
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pantalla.fill(BLANC)
    #dibuixem el text a la posició 200,200
    pantalla.blit(img, (200, 200))
    pantalla.blit(img2, (200, 400))


    pygame.display.update()
```
