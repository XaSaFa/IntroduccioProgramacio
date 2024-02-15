# Arrays

Els arrays són un tipus de variables que poden guardar més d'un valor. A Python un array es diu també list (llista).

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/d2c6ad20-84a0-4f3f-9ff4-f65f848ba3db)

Per exemple anem a fer un array amb 9 cadenes de caràcters:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
print(comunitat)
```

## Accedir a un element individual d'un array:

Aquest array té 9 elements diferents, per exemple, el primer element "Gandalf" és accessible com comunitat[0]:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
print(comunitat[0])
```

Aquest programa imprimirà la paraula que hi ha al primer element de l'array (element 0), que és Gandalf.

Per exemple per accedir a l'últim element ho faríem amb comunitat[8], per que sabem quants elements té l'array.

## Coneixer la longitud d'un array:

Per saber quants elements té un array utilitzem la funció len().

Així que len(comunitat) ens retornarà 9 perquè hi ha 9 elements. 

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
print(len(comunitat))
```

**IMPORTANT:**

En un array de 9 elements el primer element serà el 0 i l'últim len()-1

Així, aquest problema donarà ERROR:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
quantitat = len(comunitat)
print(comunitat[quantitat])
```

El podem arreglar així:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
quantitat = len(comunitat)
ultim = quantitat - 1
print(comunitat[ultim])
```

## Accedir a tots els elements d'un array:

Per accedir a tots els elements d'un array normalment utilitzem un bucle for. Per exemple per imprimir tots els elements de comunitat fem:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
for i in range(0,len(comunitat)-1):
    print(comunitat[i])
```

Però Python té una forma més fàcil d'accedir als elements d'un array:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
for i in comunitat:
    print(i)
```

El que fa Python és fer que la variable i prengui el valor de cada element de comunitat de forma ordenada.

## Treure elements d'un array:

Puc eliminar un element de l'array amb la funció pop().

Per exemple, per eliminar l'element primer de l'array faria:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
comunitat.pop(0)
print(comunitat)
```

Si volem podem guardar el valor de la variable que eliminem de l'array:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
mort = comunitat.pop(0)
print(comunitat)
print(mort)
```

Podem eliminar un element d'un array per el seu valor amb la funció remove():

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
comunitat.remove("Gandalf")
print(comunitat)
```

Només s'elimina la primera aparició de Gandalf de l'array, si hi hagués dos elements iguals no s'eliminaria el primer.

## Afegir elements a un array:

Podem afegir elements al final d'un array amb la funció append(). 

Per exemple, afegiré elements a un array buit:

```
comunitat = []
comunitat.append("Frodo")
print(comunitat)
comunitat.append("Sam")
print(comunitat)
```

## Ordenar un array:

La funció sort() ordena alfabèticament un Array.

Exemple:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
comunitat.sort()
print(comunitat)
```

També podem ordenar una llista al revés:

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
comunitat.sort(reverse=True)
print(comunitat)
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

- Tenim la llista següent: comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"] fes un programa que mostri:

1. El primer element.
2. L'últim element.
3. L'element del mig.
4. L'element que alfabèticament va primer.
5. L'element que alfabèticament va darrer.
6. Elimina "Aragorn" de la llista y mostra l'element que va alfabèticament primer.
7. Afegeix "Arwen" a la llista y mostra la llista ordenada alfabèticament.

**Solució:**

```
comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
print(comunitat[0])
print(comunitat[len(comunitat)-1])
print(comunitat[int(len(comunitat) / 2)])
comunitat.sort()
print(comunitat[0])
print(comunitat[-1])
comunitat.remove("Aragorn")
print(comunitat[0])
comunitat.append("Arwen")
comunitat.sort()
print(comunitat)
```
🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎



