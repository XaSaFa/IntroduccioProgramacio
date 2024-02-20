# Funcions a Python

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/8f7e4a43-06e8-494c-b14a-f266e98e6c45)

Les funcions són troços de codi ue s'executen quan són cridades.

Poden tenir paràmetres, que és informació que se li passa a la funció.

També poden retornar valors que es necessiten per seguir executant un programa.

## Funció bàsica:

```
def digues_hola():
  print("Hola")
```

Aquesta funció es diu digues_hola() i fa un print de la paraula hola.

## Cridar una funció:

Una funció es pot cridar pel seu nom.

```
def digues_hola():
  print("Hola")

digues_hola()
```

## Paràmetres a una funció:

Una funció pot rebre valors per tal d'executar-se, aquests valors s'anomenen paràmetres.

Exemple, aquesta funció rep una paraula i la imprimeix per pantalla:

```
def repeteix_paraula(paraula):
  print(paraula)

repeteix_paraula("hola")
```

Al executar-se li passem com argument la paraula "hola", així que, com a resultat imprimirà hola.

Exemple, aquesta funció rep dos numeros i imprimeix la seva suma:

```
def suma_dos_numeros(num1, num2):
  print(num1+num2)

suma_dos_numeros(10, 6)
```

Aquesta funció rep els números 10 i 6 i imprimeix la seva suma 16.

## Retorn de valor:

Una funció que retorna un valor fa servir la paraula return.

A l'exemple següent tenim una funció anomenada suma_numeros que rep dos numeros i retorna la seva suma:

```
def suma_numeros(num1, num2):
  return num1+num2

print(suma_numeros(10, 6))
```
