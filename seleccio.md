# Selecció

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/bc23f03c-d12f-4f6b-b442-1826ab0a83f0)

La selecció es dona quan tenim més d'una opció que es pot donar en un codi.

Llavors el programa executarà unes comandes si es compleix la condició i unes altres comandes en cas contrari.

## IF ELSE

```
a = 2
if a < 5:
    print("El número és menor que 5.")
else:
    print("El número és major que 5.")
```

Aquest codi mostra que es compleix una condició **a < 5** i el que farà serà imprimir "El número és menor que 5.", tot el codi que està dins de else no s'executa.

En cas de que el número fos més gran que 5, per exemple amb a = 10, s'executarà el codi que hi ha dins de else però no el codi de if, és a dir, es mostra per pantalla "El número és major que 5.".

Tenim un cas especial, que és **a = 5**, en aquest cas **COM NO ES COMPLEIX a < 5** el programa donarà una resposta errònia: "El número és major que 5.".

## ELIF

Per evitar el problema del codi anterior podem afegir condicions adicionals de dues formes (ficant un altre if dins de else) o utilitzant ELIF.

ELIF és una selecció que s'executa quan no es compleix la condició inicial IF.

Exemple, per solucionar el problema anterior:

```
a = 2
if a < 5:
    print("El número és menor que 5.")
elif a == 5:
    print("El número és igual a 5.")  
else:
    print("El número és major que 5.")
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
**Activitat:**

1. Discoteca Cosmos: Fes un programa que pregunti a l'usuari la seva edat i si és major d'edat li digui que pot entrar i que no pot entrar en cas contrari.
2. Fa fred: Fes un programa que pregunti la temperatura, en cas de fer menys de 15 graus et digui "agafa una jaquesta que refresca", en cas contrari diu "quin temps més bo que fa".
3. Login: Fes un programa que tingui un usuari i una contrasenya guardades. El programa demanarà usuari i contrasenya a l'usuari i si són autèntiques donarà la benvinguda al sistema, en cas contrari indicarà que hi ha un error d'autenticació.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
