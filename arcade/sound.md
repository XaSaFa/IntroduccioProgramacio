# So a pygame

Un dels elements fundamentals dels videojocs és el so.

Pygame permet reproduir sons fàcilment amb els mòduls [mixer](https://www.pygame.org/docs/ref/mixer.html) i [mixer.music](https://www.pygame.org/docs/ref/music.html).

Mixer serveix per sons i mixer.music és més aviat per a tenir una música de fons.

## Exemple

Agafem per exemple aquesta cançó en mp3 - [Música](music.mp3).

Podem crear un programa que reproduceixi la cançó d'aquesta manera:

```
import pygame

pygame.init()
ambient_music = pygame.mixer.Sound('assets/music.mp3')
ambient_music.play()
while True:
    pass
```

O d'aquesta:

```
import pygame
import time

pygame.init()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play()
while True:
    time.sleep(3)
    break
```

S'ha de tenir en compte que per que la música es reprodueixi el programa ha d'estar en execució, per això tenim el bucle.

La música es reproduirà una vegada i finalitzarà.

Podem ajustar la quantitat de vegades que es reprodueix una música amb la crida a la funció play.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/7d0ee2de-0ff4-4220-9f1c-c3cd66d6a631)

Així si volem que la música es reprodueixi per sempre utilitze, el valor de loop = -1.

## Fadeout:

Un Fadeout és un efecto que fa que la música vagi desapareixent poc a poc.

Per exemple el següent programa reprodueix 10 segons de música i després fa un fade out de 3 segons (3000 milisegons).

```
import pygame
import time

pygame.init()
ambient_music = pygame.mixer.Sound('assets/music.mp3')
ambient_music.play()
while True:
    time.sleep(10)
    ambient_music.fadeout(3000)
    break
```

## Volum

El volum es pot ajustar en volum de valor 0 a valor 1 que és el màxim.

Aquí tenim un programa que va pujant el so des del 20% fins al 100%:

```
import pygame
import time

pygame.init()
ambient_music = pygame.mixer.Sound('assets/music.mp3')
ambient_music.play()
while True:
    ambient_music.set_volume(0.2)
    time.sleep(3)
    ambient_music.set_volume(0.4)
    time.sleep(3)
    ambient_music.set_volume(0.6)
    time.sleep(3)
    ambient_music.set_volume(0.8)
    time.sleep(3)
    ambient_music.set_volume(1)
    time.sleep(3)
    ambient_music.stop()
    break
```

Si volguèssim podríem fer que el so es reproduís a un volum diferent per l'altaveu esquerre i el dret:

```
import pygame
import time

pygame.init()
ambient_music = pygame.mixer.Sound('assets/music.mp3')
music_chanel = pygame.mixer.Channel(0)
ambient_music.play()
while True:
    ambient_music.set_volume(1)
    time.sleep(3)
    music_chanel.set_volume(1,0)
    time.sleep(3)
    music_chanel.set_volume(0,1)
    time.sleep(3)
    music_chanel.stop()
    break
```
