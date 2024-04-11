# Vides

```
# vides:
vides1 = 3
vides2 = 3
vida_image = pygame.image.load('assets/cor.png')
vida1_jugador1 = vida_image.get_rect(midbottom=(300,180))
vida2_jugador1 = vida_image.get_rect(midbottom=(280,180))
vida3_jugador1 = vida_image.get_rect(midbottom=(260,180))
```
# Dibuixar vides

Després de dibuixar els jugadors.

```
    #dibuixar vides:
    pantalla.blit(vida_image, vida1_jugador1)
    pantalla.blit(vida_image, vida2_jugador1)
    pantalla.blit(vida_image, vida3_jugador1)
```
