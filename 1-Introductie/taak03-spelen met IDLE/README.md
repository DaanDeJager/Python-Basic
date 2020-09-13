# PYTHON BASICS-TAAK-03

## Spelen met IDLE

### Uitleg en opdrachten

Let op, tussen de tekst van de uitleg staan ook de opdrachten. Dit omdat je dan
makkelijk de opdrachten kunt koppelen met de uitleg.

We gaan nog even verder met strings

We kunnen allerlei bewerkingen uitvoer op strings.

\>\>\>’Py’’thon’

Levert op: ‘Python’

\>\>\>’Py’+’thon’

## Levert op: ‘Python’

En: \>\>\>3\*’Py’+2\*’thon’

Levert op: ‘PyPyPythonthon’

Een methode die je nog wel kent van javaScript en PHP is de functie len(). Het
werkt in Python net als je verwacht. Dus:

Len(‘hottentottententententoonstelling’)

Levert op: 33

Ook als je eerst een variabele initialiseert met een string en daarna de len()
uitvoert, werkt het zoals je verwacht. Een voorbeeld:

\>\>\>a = ‘negenennegentig’

\>\>\>len(a)

Levert op: 15

### Type conversion

Type conversion is waar het éne datatype wordt omgezet naar een ander.

Implicit conversion is waar dit door de interpreter zèlf gebeurt. Bijvoorbeeld
door een deling.

Explicit conversion is waar dit expliciet, door de code van programmeur wordt
gedaan. Dit wordt ook wel Type Casting genoemd.

**Opdracht:**

*Lever de statements die bij de opdrachten horen in in TEAMS*  

Converteer een string naar een geheel getal met behulp van int()

- werkt dit ook met letters?
- werkt dit ook met een string als ‘56.87’
- Wat gebeurt er in deze gevallen?
- Hoe zou je een expliciete conversie van een string als ’56.87’ naar een
 getal uitvoeren?

Het is natuurlijk ook mogelijk om overal een string van te maken.

- Doe dat eens voor een integer en een float.
 Zijn hier restricties voor het getal dat je wilt converteren?
Nee
**Opdracht:**

Neem deze twee getallen: 162.48 en 13.54. Deel 162.48 door 13.45. Maak een
integer van de uitkomst. En maak daar vervolgens een string van.

162.48 / 13.45

Ondertussen wordt het handiger om een programmafile te maken dan om alles
interactief in IDLE te doen. We maken dan een tekstfile aan die we kunnen editen
met een (syntax) editor.  
Zo’n tekstfile kunnen we aanmaken, opslaan, lezen en wijzigen (editen). 
We kunnen deze tekstfile vervolgens laten lezen door Python dat het dan regel
voor regel gaat lezen en uitvoeren.

We kunnen iedere editor gebruiken die we willen:

- We kunnen editen in VSCODE
- En ook in ATOM
- Of in Sublime tekst
- Of in de IDLE Shell
- Of in notepad++
- Of … vul je eigen voorkeur maar in.

Weet je het nog? In de Getting Started sectie op www.python.org vindt je hele
lijsten met editors.
<https://www.python.org/about/gettingstarted>

### In de “native” python omgeving: de Python Shell (IDLE)

Bovenaan in het IDLE window ga je naar “File”; klik op New File en geef het
bestand een naam. Er opent een nieuw window. In dit window typ je de python
programmacode, regel voor regel. Je zult zien dat in dit window syntax
highlighting plaatsvindt. IDLE herkent de syntax en geeft dat aan door middel
van kleurtjes. En je ziet dat het shell window waar we eerst in werkten ook
gewoon open blijft staan. Hier komt de programmauitvoer in terecht. 
Ben je klaar met het editen van jouw code, dan sla je de file op. (ctrl + S) of
via het file menu. Daarna ga je in het menu naar “Run”. Python leest nu jouw
opgeslagen file en geeft het als input aan de interpreter. Dat zie je gebeuren
in de Python Shell. De programmauitvoer komt, samen met eventuele foutmeldingen,
in het Shell window terecht.  
Deze werkwijze heeft een voordeel: de koppelingen tussen de Python shell, de
interpreter en jouw programmabestand werken zonder dat je daar iets extra’s voor
moet doen.

## Leerdoelen

- Ik weet wat de python Shell is.

- Ik kan er interactief mee werken

- ik weet wat impliciete en expliciete type conversion is.

- Ik kan explicitete conversie (type casting) toepassen.

- Ik weet hoe ik een programmafile kan aanmaken in IDLE

- Ik weet hoe ik een programma kan opslaan met behulp van IDLE

- Ik weet hoe ik een programma kan aanpassen in IDLE

- Ik weet hoe ik een programma kan uitvoeren met IDLE

## Bronnen

Maak er een gewoonte van om de bron te raadplegen bij vragen over syntax. In dit
geval is dat: <https://docs.python.org/3/reference/index.html>

Alles over python: <https://www.python.org>

Python datatypen: Python.org: <https://docs.python.org/3/library/datatypes.html>

Tutorials over python (Engelstalig) Python.org:
<https://docs.python.org/3/tutorial/index.html>

For loops in python: <https://pythonforloops.com>

Of: <https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp>
