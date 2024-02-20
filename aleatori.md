# Generar números aleatoris

Per generar números aleatoris utilitzem la llibreria **random** de Python.

Els números són pseudo-aleatoris, això vol dir que en realitat depenen d'una llavor "seed" per a generar la resta de números, normalment agafen l'hora del sistema.

Aquest programa genera un número aleatori del 1 al 10 (ambdós inclosos):

```
import random

print(random.randint(1, 10))
```
