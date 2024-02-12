# String

Una cadena de text o string és un tipus de variable que s'utilitza molt a programació.

Els strings són una successió de caràcters alfanumèrics, és a dir, lletres i números, però també d'altres caràcters especials.

En realitat Python utilitza els caràcters de la codificació [UTF-8](https://www.fileformat.info/info/charset/UTF-8/list.htm?start=1024).

Veiem un exemple de string:

```
nom = "Pep"
print (nom)
```

Aquí la variable nom té el valor Pep i el programa el mostra.

Podem fer que un string tingui més d'una línia, per exemple:

```
simbol = """*
**
***"""
print(simbol)
```

Aquesta variable té 3 línies i al fer print les veurem tal i com estan escrites, això es fa amb un triple parèntesis.

## Longitud d'un string

Per saber quants caràcters té un string utilitzem la funció len().

```
frase = "Hola Xavi"
print(len(frase))
```

La funció len em retorna 9, que són els caràcters que té ka frase.

## Comprovar si hi ha una subcadena dins d'una cadena de caràcters

De vegades volem saber si hi ha una paraula dins una frase, això ho fem així:

```
frase = "Es el alcalde el que escoge a los vecinos."
print("alcalde" in frase)
```

Aquest programa retorna True per què la paraula alcalde és dins de la cadena frase, si no estigués retornaria False.

També podem fer l'exemple contrari amb not in:

```
frase = "Es el alcalde el que escoge a los vecinos."
print("alcalde" not in frase)
```

Aquest programa retornarà False.

## Concatenar strings

Quan volem unir dos o més strings utilitzem l'operador suma, el +.

Exemple, si tinc dos variables string i vull crear una variable que sigui la concatenació de les dues, és a dir, la seva unió, faig:

```
paraula1 = "Hello "
paraula2 = "World!"
frase = paraula1 + paraula2
print(frase)
```

Aquest programa retorna la concatenació de les dues variables, és a dir, Hello World!

**IMPORTANT:** 

Si utilitzem + però una de les variables és un número donarà error, haureu de transformar la variable en una cadena de text amb la funció str, exemple:

```
paraula1 = "Avui és dia "
paraula2 = 5
frase = paraula1 + str(paraula2)
print(frase)
```


🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Fes un programa que pregunta a l'usuari el número del DNI, després pregunta la lletra del DNI i et retorna la frase "El teu DNI és " seguit de la concatenació del número i lletra del DNI.
2. Fes un programa que pregunta un número de telèfon i contesta "El número és vàlid" si té 9 caràcters i "El número no és vàlid" en cas contrari.
3. Fes un programa que pregunta una llista de paraules a l'usuari indefinidament (en bucle) i quan l'usuari introdueix la paraula "final" mostra la concatenació de totes les paraules (menys final).

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

## Tallar strings:

Un array es pot retallar entre dues posicions, per exemple si tenim la paraula "desesperança", la podem retallar així:

```
paraula = "desesperança"
print (paraula[3:])
```

Això talla la paraula des de la lletra 3 fins el final, també podem aconseguir el mateix amb:

```
paraula = "desesperança"
print (paraula[3:12])
```

O amb:

```
paraula = "desesperança"
print (paraula[3:len(paraula)])
```

## Escapar caràcters:

Si volem que un string contingui caràcters especials com les cometes ", les hem d'escapar, és a dir, indicar que són un caràcter.

Per exemple, això provocarà un error:

```
text = "Gandalf dijo: "El verdadero coraje no consiste en saber cuándo quitar una vida, sino cuándo perdonarla."
print(text)
```

Per arreglar-lo escapem les cometes dins del text així:

```
text = "Gandalf dijo: \"El verdadero coraje no consiste en saber cuándo quitar una vida, sino cuándo perdonarla.\""
print(text)
```

## Passar una cadena de text a majúscules:

Ho fem amb la funció upper():

```
a = "Hello, World!"
print(a.upper())
```

## Passar una cadena de text a minúscules:

Ho fem amb la funció lower():

```
a = "Hello, World!"
print(a.lower())
```

## Treure espais en blanc:

Els espais en blanc al principi i al final d'una cadena es poden treure amb la funció strip():

```
a = " Hello, World! "
print(a.strip())
```

## Canviar elements d'una cadena:

Podem reemplaçar elements d'una cadena amb la funció replace():

```
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Separar elements d'una cadena:

Podem separar elements d'una cadena amb la funció split(). 

Aquesta funció crea una llista de tots els elements separats per un caràcter.

```
a = "Hello, World!"
b = a.split(",")
print(b)
```

## Funcions de cadena de text:

Existeixen moltes funcions que ens ajuden a treballar amb strings, aquí teniu unes quantes:

[https://www.w3schools.com/python/python_strings_methods.asp](https://www.w3schools.com/python/python_strings_methods.asp)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Fes un programa que demani una frase a l'usuari i la mostri en majúscules i després en minúscules.
2. Fes un programa que demani una frase i canviï totes les lletres 'a' per '*'.
3. Fes un programa que demani una frase i crei una llista de les paraules, després mostrarà la llista.
4. Fes un programa que demana una paraula i mostra només la primera i l'última lletra.
5. Fes un programa que demana una frase i compta quantes vegades apareix una lletra (la lletra la demana també a l'usuari).
6. Comprova si una paraula introduïda per l'usuari és un palíndrom.
7. Fes un programa que demani una paraula i transformi la primera i última lletres en majúscules.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

