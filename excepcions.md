# Control d'excepcions

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/74670f33-6fe7-4c95-835b-ab1ff39fa496)

Quan un programa provoca un error Python ens mostrarà un error i el programa pararà la seva execució.

Exemple:

```
print(x)
```

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/3c73b59d-3999-48b9-9ec3-e99b8ff894d4)

Per evitar-ho utilitzem les comandes try i except.

Exemple:

```
try:
  print(x)
except:
  print("An exception occurred")
```

# Com funciona?

Quan tenim un codi que pot provocar un error el col·loquem dins d'un bloc try.

Per gestionar l'error col·loquem codi dins del bloc except, aquest codi s'executarà quan s'hagi produït un error dins del codi de try.

<img src="https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/eae38680-0c60-4c84-91a5-cc840330fe8a" width="500px">

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Pregunta a l'usuari dos nombres i divideix-los. Utilitza un bloc try i except per evitar l'error de divisió per zero.
2. Demana a l'usuari que introdueixi un número, i intenta convertir aquesta entrada en un enter. Utilitza try i except per capturar qualsevol error de conversió.
3. Pregunta a l'usuari dos valors i intenta sumar-los. Utilitza try i except per capturar errors quan els valors no són números.
4. Crea una llista amb alguns elements i demana a l'usuari un índex. Utilitza try i except per gestionar l'error que es produeix quan l'índex no existeix a la llista.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Solució:**

```
# 1. Pregunta a l'usuari dos nombres i divideix-los. Utilitza un bloc
# try i except per evitar l'error de divisió per zero.

# num1 = input("Introdueix el primer nombre: ")
# num2 = input("Introdueix el segon nombre: ")
# try:
#     resultat = int(num1) / int(num2)
#     print("El resultat de la divisió és: ",resultat)
# except:
#     print("Error els numeros no son correctes o el segon numero es un zero.")

# 2. Demana a l'usuari que introdueixi un número, i intenta convertir
# aquesta entrada en un enter. Utilitza try i except per capturar
# qualsevol error de conversió.

# entrada = input("introdueix el num: ")
# try:
#     salida = int(entrada)
#     print(salida)
# except:
#     print("Error de entrada")

# 3. Pregunta a l'usuari dos valors i intenta sumar-los. Utilitza try i
# except per capturar errors quan els valors no són números.

# num1 = input("digues un numero")
# num2 = input("digues un altre numro")
# try:
#     resultat = float(num1) + float(num2)
#     print(resultat)
# except:
#     print("Error")

# 4. Crea una llista amb alguns elements i demana a l'usuari un índex.
# Utilitza try i except per gestionar l'error que es produeix quan
# l'índex no existeix a la llista.

# llista=[1,3,4,7,9]
# index=input("Quin element vols mostrar? ")
# try:
#     print(llista[int(index)])
# except:
#     print("Aquest element no hi és ")
```
