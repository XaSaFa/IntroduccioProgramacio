# Els llenguatges de programació

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/708d3143-c7f3-42c6-b6b6-23978a4361a6)

Els ordinadors són màquines creades per a processar informació mitjançant la CPU (Central Porcess Unit). 

Els ordinadors actuals són màquines electròniques alimentades per electricitat, per aquest motiu només entenen dos tipus d'informació: els zeros i els uns.

Per aquest motiu diem que els ordinadors entenen el llenguatge binari. En concret es fan servir unes seqüències de dígits anomenades llenguatge màquina.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/3d325183-5bb4-4d36-9dfe-9f28c4ceddd9)

- [Vídeo de com programar el ALTAIR](https://www.youtube.com/watch?v=EV1ki6LiEmg)
- [Evolució llenguatges de programació - 1](https://www.technolush.com/blog/evolution-of-programming-languages)
- [Evolució llenguatges de programació - 2](https://tecky.io/zh_Hant/blog/evolution-of-programming-languages/)

## Llenguatge Assembler

Cada instrucció de la CPU té un número corresponent per identificar-la, que és el que entén el processador.

Segons el tipus d’instrucció la CPU també espera trobar els paràmetres per executar-la.

Aquestes instruccions són una sèrie de uns i zeros que només entén l’ordinador i es coneix amb el nom de “Codi Màquina”.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/a10e63d4-bf3e-4ff2-97fa-ef53eb1fd04a)

El Codi Màquina és molt difícil d’entendre per les persones, per això es va inventar el llenguatge assemblador.

El llenguatge assemblador utilitza codificació mnemotècnica per representar les instruccions. 

**Per exemple:**

ADD EAX, 10 (suma 10 al valor dins registre EAX, emmagatzema el resultat a EAX).

Els programes escrits en codi assemblador es poden passar a codi màquina amb l’ajuda d’un ensamblador.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/4f44c5e1-86dc-4fc0-91e9-a10d52e7c209)

## Els llenguatges compilats

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/ec0223ed-d0c9-46b9-9ab9-9f0d57dfac3b)

Als llenguatges compilats s’utilitzen **llenguatges d’alt nivell** que la màquina no pot processar.

Per a que la màquina ho entengui el codi font d’alt nivell ha de passar a codi màquina, aquest procés el fa un programa anomenat **compilador**.

El **codi font** és el codi en llenguatge d’alt nivell escrit per un programador/a.

El compilador no és més que un traductor entre el llenguatge d’alt nivell i el codi màquina, entre el que entenen les persones i el que entén la CPU.

Si hi ha errors en el codi font el compilador donarà errors de compilació i no es generarà el codi màquina executable.

## Els llenguatges basats en màquines virtuals

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/108acdcf-c573-4b0f-8032-736d917002da)

Hi ha tota una família de llenguatges requereixen de l’ús de la figura de la màquina virtual. Aquesta màquina virtual té un codi màquina propi, diferent de qualsevol arquitectures real (p.ex. x64 ).

El procés en aquests llenguatges és el següent:

1. El llenguatge original es compila, però no a codi màquina real sinó a codi màquina de la màquina virtual.  Aquests arxius compilats contenen el que es coneix com a Byte-Code o Intermediate Language. 

2. Per executar el bytecode o IL, fa falta un altre programa (el que fa el paper de màquina virtual), que s’encarrega d’executar-lo. El procés que fa es habitualment el que es coneix com Just-in-time compilation (s’abreuja JIT), que és un sistema que està a mig camí de la compilació i la interpretació de codi. La idea és que el bytecode es va traduint a mesura que fa falta, però hi ha una cache per no tornar a traduir codi que s’hagués traduït anteriorment.

Un dels grans avantatges del model de màquina virtual, és que permet una total portabilitat del codi, Sempre i quan algú ens doni una implementació de la màquina virtual en la plataforma que necessitem, el codi font de la nostra aplicació sempre serà el mateix.

## Els llenguatges interpretats

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/5acf72ff-c950-4930-9081-bf23c8ec4d5d)

En el cas dels llenguatges interpretats, també es parteix d’un llenguatge d’alt nivell, però en aquest cas no es tradueix tot de cop i s’executa directament el codi màquina sinó que l’interpret (un altre programa) s’encarrega d’anar executant indirectament el codi instrucció per instrucció.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

Activitat per grups de 3 persones: 

Feu una presentació amb la següent informació.

0. Expliqueu breument cada tipus de llenguatge (compilat, interpretat i de MV). 
1. Poseu de 3 a 5 exemples de llenguatges de cada tipus.
2. Cada membre del grup busca el codi font d'un programa "Hello Word" en un dels llenguatges que heu trobat, un per cada tipus.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎


