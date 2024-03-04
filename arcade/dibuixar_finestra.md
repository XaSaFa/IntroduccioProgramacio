# Dibuixar finestra

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/b06ec08c-dda5-40f8-9b87-eb1b7b23aade)

Una finestra de joc té certs components que s'han de definir abans de poder dibuixar-se.

- Icon: És una icona que es mostra a l'esquerra de la finestra, normalment representa d'alguna manera el programa, és com un logo.
- Caption: És un text, el títol que tindrà la finestra.
- Amplada: S'ha de definir l'amplada que tindrà la finestra.
- Alçada: Alçada que tindrà la finestra.
- Color de fons: Podem omplir una finestra amb un color.
- Imatge de fons: Podem dibuixar una imatge que serà el fons de la finestra.

```
# import the pygame module, so you can use it
import pygame

WIDTH = 640
HIGH = 480
LOGO_IMAGE = "assets/moon.png"
CAPTION_TEXT = "My Space Game"
# create a surface on screen that has the size of 640 x 180
screen = pygame.display.set_mode((WIDTH, HIGH))

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(LOGO_IMAGE)
    # set the caption of the screen
    pygame.display.set_caption(CAPTION_TEXT)
    # set the logo of the screen
    pygame.display.set_icon(logo)
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # background set to BLACK
        screen.fill((0, 0, 0))
        # draw the screen
        pygame.display.flip()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
```

## Tamany de la finestra

Tot i que definirem un tamany de finestra amb la seva **amplada** i **alçada** també podem fer que la finestra ocupi tota la pantalla amb el mode **FULLSCREEN**, cosa que farà que tots els elements dibuixats de la finestra s'escalin per ocupar tota la superfície de la pantalla de l'ordinador.

## Assets del projecte

El nostre projecte serà un videojoc, per aquest motiu comptarà amb fitxers d'imatge i so. 

Aquests fitxers els guardarem dins una carpeta anomenada assets al nostre projecte.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/23d4ac69-982a-434c-9b06-277c7dca85e4)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Crea una finestra amb una icona d'un animal, de títol "Zoo X" on X és el teu cognom, tamany 320x200 i color de fons groc.
2. Crea una finestra amb una icona d'un peix, de títol "Ocean X" on X és el teu cognom, tamany 640x480 i color de fons blau.
3. Crea una finestra amb una icona d'un planeta, de títol "Space X" on X és el teu cognom, tamany 1280x720 i color de fons gris.
4. Crea una finestra amb una icona d'un tanc, de títol "War X" on X és el teu cognom, tamany 800x600 i color de fons verd.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
