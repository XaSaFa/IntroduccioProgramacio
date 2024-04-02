![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/e89d1757-5bf8-4db0-8555-96e67e6d4bbe)# FPS (Frames Per Second)

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/6be74fad-a853-4712-b285-793bce802ffd)

Els FPS és la mesura en productes audiovisuals com pel·lícules o videojocs de quantes **imatges es mostren en un segon**.

Quantes més imatges per segon es mostrin, més realista i suau serà el moviment a la pantalla.

Al mon dels videojocs es considera una tasa de FPS acceptable entre 30 i 60, podent superar-se els 60 fps.

## Com controlar els fps a pygame?

A pygame els fps seran la quantitat de vegades que executem un codi determinat en un segon, cosa que es podrà cumplir si l'ordinador on s'executa el codi és prou ràpid.

Primer s'ha d'**indicar el nombre de fps abans de començar el bucle del joc**.
```
# Control de FPS
clock = pygame.time.Clock()
fps = 60
```

I després indiquem que ha passat un frame al final del bucle amb:

```
clock.tick(fps)
```

