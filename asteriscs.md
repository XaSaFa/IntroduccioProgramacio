# ASTERISCS

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/d7636e11-0fe7-4b72-a746-8d915abe147f)

## 1.- Moviment

Hem de fer un programa que imprimeixi per pantalla un asterisc.

L'asterisc es podrà moure amb les tecles "a" i "d" d'aquesta forma:

- "a": L'asterisc es mou una posició a l'esquerra, però no pot mourès a una posició negativa.
- "d": L'asterisc es mou una posició a la dreta, però no pot mourès a una posició superior a 20.

Així simulem un joc en el que un asterisc es mou en una pantalla d'un caràcter d'alçada per 20 d'ample.

El joc no acaba, és un bucle continu.

```
posicio_asterisc = 0
AMPLADA = 20
while True:
    #genero cadena de text amb l'asterisc a la seva posició:
    cadena_asterisc = ""
    for i in range(AMPLADA):
        if posicio_asterisc == i:
            cadena_asterisc += "*"
        else:
            cadena_asterisc += " "
    #imprimerixo l'asterisc:
    print(cadena_asterisc)

    #demano el moviment al user:
    moviment = input("")

    #aplico el moviment de l'usuari:
    if moviment == 'a' and posicio_asterisc > 0:
            posicio_asterisc -= 1
    elif moviment == 'd' and posicio_asterisc < AMPLADA:
            posicio_asterisc += 1
```

## 2.- Vides

El programa pregunta al principi quantes vides tenim.
Les mostra per pantalla.

Si pressionem la tecla "k" es perd una vida.

Si les vides arriben a zero el programa mostra "Game Over" i surt.

