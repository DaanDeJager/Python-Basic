# PYTHON BASIC Functies02

## Passing parameters

### Uitleg

Het doel is hier om een functie te schrijven die een input van de user
verwerkt.

We bouwen hier voort op de laatste functie van de vorige taak.

- Eerst moeten we een user input mogelijk maken.

- Dan die string gereed maken voor verwerking in de functie

- De functie uitvoeren met het doorgeven van parameters

- En het resultaat aan de gebruiker teruggeven.

### Input()

Python kent een statement waarmee input gevraagd wordt. We maken hier gebruik
van de syntax:

a = input(‘prompt’)

Houd er rekening mee dat alle input die hier wordt gegeven een string wordt. a
is dus altijd een string.

### Opdracht

De bedoeling is dat de functie een temperatuur gaat omrekenen van °C naar °F of
van °F naar °C, afhankelijk van de input.  
Geeft de gebruiker als input 37 C (of
37C, of 37 c, of 37c) dan wordt omgerekend naar Fahrenheit.  
Geeft de gebruiker als input 100 F (of 100F, of 100f, of 100 f) dan wordt de
input omgerekend naar Celcius.
temp = input("input temp:")
degree = int(temp[:-1])
convert = temp[-1]

if convert.upper() == "C":
  result = (9 * degree) / 5 + 32
  graden = "Fahrenheit"
elif convert.upper() == "F":
  result = (degree - 32) * 5 / 9
  graden = "Celsius"

print("The temp", graden, "is", result,)


#### Decompositie (uiteenrafelen in verschillende stappen die uitgevoerd moeten worden)

1. De input vragen aan de gebruiker. (eventueel uitleggen wat die moet doen)

2. Met een string kunnen we niet rekenen, dus moeten we er een getal van maken,
    maar ook

3. Vaststellen of het hier om Celcius of Fahrenheit gaat.

4. De juiste parameters doorgeven aan de functie: Het getal èn of de input °C
    of °F betreft

5. De juiste berekening uitvoeren in de functie

6. Het resultaat van de berekening teruggeven

7. Het resultaat aan de gebruiker laten zien

Decompositie (of probleem analyse) is één van de belangrijkste stappen in
programmeren. Hier bepaal je hoe het programma er in grote lijnen uit gaat
zien en welke onderdelen je moet realiseren om het geheel te laten werken.

Het maken van een goede compositie bepaalt (in eerste instantie) het succes
van de code die je gaat maken.

Zonder goede decompositie heb je geen idee wat je moet doen, laat staan dat
je het de computer kunt vertellen.

Op basis van zo’n decompositie kun je al een flowchart maken die laat zien
hoe het programma zou moeten werken. Op basis van zo’n decompositie weet je
ook welke statements en functies je waarschijnlijk nodig gaat hebben. En
daar kun je dan online de juiste syntax bij zoeken.

**Opdracht**: Maak een flowchart van deze decompositie. Of, als je een
andere manier weet om het doel te bereiken, dan maak je daar een flowchart
van.

De input is een string, daar moet je dus een getal van maken. Maar int(’35
C’) gaat niet werken. Probeer het maar in IDLE. En we moeten ook nog
vaststellen of het hier Celcius of Fahrenheit betreft.

**Tip**: Met de index [-1] krijg je alleen het laatste letterteken van de
string.

Met de index [:-1] krijg je alle lettertekens tot aan het laatste teken van
de string

Als je dit toepast kun je twee variabelen maken en die doorgeven aan de
functie. De functie moet dan zelf uitzoeken welke omrekeningsformule moet
worden gebruikt:

**Formules**:  
F to C : c = ( f - 32) \* 5 / 9  
C to F : f = c * 9 / 5  + 32

Wanneer je dit programmaatje (of elk ander programma) gaat coderen, onthoudt
dan: Keep It Simple.  
Dit hele programma is ongeveer 20 regels code lang.

### Leerdoelen

- Ik kan een gebruiker om input vragen

- Ik kan indexen toepassen om delen van de strring te krijgen

- Ik kan de input splitsen in een string en een getal

- Ik kan een functie aanroepen met twee parameters

- Ik kan condities toepassen zodat de juiste berekening wordt uitgevoerd

- Ik kan een waarde teruggeven uit een functie

### Eindresultaat

Als het programma wordt uitgevoerd is de schermuitvoer ongeveer zoals dit:

Geef een waarde in C of F als 37C of 100F :212f

Het gaat hier om 212 graden F

Het resultaat is: 100.0 C

### Bronnen

<https://www.w3schools.com/python/ref_func_input.asp>

<https://realpython.com/lessons/string-indexing>

<https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3>
