# Generar números aleatoris

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/e8d85acb-fec1-432f-aa16-0bf183ae7289)

Per generar números aleatoris utilitzem la llibreria **random** de Python.

Els números són pseudo-aleatoris, això vol dir que en realitat depenen d'una llavor "seed" per a generar la resta de números, normalment agafen l'hora del sistema.

Aquest programa genera un número aleatori del 1 al 10 (ambdós inclosos):

```
import random

print(random.randint(1, 10))
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitat:**

1. Crea un programa que faci una tirada de dau de 6 cares.
2. Crea una funció anomenada dau_6 que faci una tirada de dau de 6 cares.
3. Crea una funció anomenada daus_6 que pregunti quants daus ha de llençar i mostri el resultat de totes les tirades de daus demanades.
4. Crea una funció anomenada dau_x que pregunti de quantes cares són els daus i faci una tirada de daus.
5. Crea una funció anomenada daus_x que pregunti les cares del dau i quants daus ha de llençar i faci la tirada dels daus.

**Solució 2-5:**

```
import random

def dau_6():
    print(random.randint(1, 6))

def daus_6():
    tirades = int(input("Quants daus vols llençar?: "))
    for i in range(tirades):
        print(random.randint(1, 6))


def dau_x():
    cares = int(input("Quantes cares té el dau?: "))
    print(random.randint(1, cares))

def daus_x():
    numero_daus = int(input("Quants daus has de llençar?: "))
    cares = int(input("Quants cares té el dau?: "))
    for i in range(numero_daus):
        print(random.randint(1, cares))
```

6. Guarda les funcions a un fitxer anomenat daus.py
   Crea un fitxer anomenat joc.py, aquest fitxer importarà el fitxer on estan les funcions de llençar daus i les cridarà per executar-se.

   Aquest fitxer mostrarà un menú amb les següents opcions:
   
  - Llençar un dau de 6 cares.
  - Llençar més d'un dau de 6 cares.
  - Llençar un dau de cares definides per usuari.
  - Llençar més d'un dau de cares definides per usuari.
  - Sortir.

**Solució 6:**

_Fitxer joc.py_
```
import daus
def mostrar_menu():
    print("""
1.-Llençar un dau de 6 cares.
2.-Llençar més d'un dau de 6 cares.
3.-Llençar un dau de cares definides per usuari.
4.-Llençar més d'un dau de cares definides per usuari.
5.-Sortir. 
    """)
while True:
    mostrar_menu()
    opcio = input("Introdueix opcio: ")
    if opcio == "5":
        break
    elif opcio == "1":
        daus.dau_6()
    elif opcio == "2":
        daus.daus_6()
    elif opcio == "3":
        daus.dau_x()
    elif opcio == "4":
        daus.daus_x()
```


🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
