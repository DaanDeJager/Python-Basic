# PYTHON BASIC-TAAK01 Functions

## Hoezo Functions?

### Uitleg

Je gebruikt al een tijdje functions, of je dat nu weet of niet. Python heeft
een heel aantal ingebouwde functions die een onderdeel van de taal zijn.
Hier zijn ze.

| **Built-in Functions**                                                         |                                                                                |                                                                             |                                                                                  |                                                                                 |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [abs()](https://docs.python.org/3/library/functions.html#abs)                  | [delattr()](https://docs.python.org/3/library/functions.html#delattr)          | [hash()](https://docs.python.org/3/library/functions.html#hash)             | [memoryview()](https://docs.python.org/3/library/functions.html#func-memoryview) | [set()](https://docs.python.org/3/library/functions.html#func-set)              |
| [all()](https://docs.python.org/3/library/functions.html#all)                  | [dict()](https://docs.python.org/3/library/functions.html#func-dict)           | [help()](https://docs.python.org/3/library/functions.html#help)             | [min()](https://docs.python.org/3/library/functions.html#min)                    | [setattr()](https://docs.python.org/3/library/functions.html#setattr)           |
| [any()](https://docs.python.org/3/library/functions.html#any)                  | [dir()](https://docs.python.org/3/library/functions.html#dir)                  | [hex()](https://docs.python.org/3/library/functions.html#hex)               | [next()](https://docs.python.org/3/library/functions.html#next)                  | [slice()](https://docs.python.org/3/library/functions.html#slice)               |
| [ascii()](https://docs.python.org/3/library/functions.html#ascii)              | [divmod()](https://docs.python.org/3/library/functions.html#divmod)            | [id()](https://docs.python.org/3/library/functions.html#id)                 | [object()](https://docs.python.org/3/library/functions.html#object)              | [sorted()](https://docs.python.org/3/library/functions.html#sorted)             |
| [bin()](https://docs.python.org/3/library/functions.html#bin)                  | [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)      | [input()](https://docs.python.org/3/library/functions.html#input)           | [oct()](https://docs.python.org/3/library/functions.html#oct)                    | [staticmethod()](https://docs.python.org/3/library/functions.html#staticmethod) |
| [bool()](https://docs.python.org/3/library/functions.html#bool)                | [eval()](https://docs.python.org/3/library/functions.html#eval)                | [int()](https://docs.python.org/3/library/functions.html#int)               | [open()](https://docs.python.org/3/library/functions.html#open)                  | [str()](https://docs.python.org/3/library/functions.html#func-str)              |
| [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint)    | [exec()](https://docs.python.org/3/library/functions.html#exec)                | [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) | [ord()](https://docs.python.org/3/library/functions.html#ord)                    | [sum()](https://docs.python.org/3/library/functions.html#sum)                   |
| [bytearray()](https://docs.python.org/3/library/functions.html#func-bytearray) | [filter()](https://docs.python.org/3/library/functions.html#filter)            | [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) | [pow()](https://docs.python.org/3/library/functions.html#pow)                    | [super()](https://docs.python.org/3/library/functions.html#super)               |
| [bytes()](https://docs.python.org/3/library/functions.html#func-bytes)         | [float()](https://docs.python.org/3/library/functions.html#float)              | [iter()](https://docs.python.org/3/library/functions.html#iter)             | [print()](https://docs.python.org/3/library/functions.html#print)                | [tuple()](https://docs.python.org/3/library/functions.html#func-tuple)          |
| [callable()](https://docs.python.org/3/library/functions.html#callable)        | [format()](https://docs.python.org/3/library/functions.html#format)            | [len()](https://docs.python.org/3/library/functions.html#len)               | [property()](https://docs.python.org/3/library/functions.html#property)          | [type()](https://docs.python.org/3/library/functions.html#type)                 |
| [chr()](https://docs.python.org/3/library/functions.html#chr)                  | [frozenset()](https://docs.python.org/3/library/functions.html#func-frozenset) | [list()](https://docs.python.org/3/library/functions.html#func-list)        | [range()](https://docs.python.org/3/library/functions.html#func-range)           | [vars()](https://docs.python.org/3/library/functions.html#vars)                 |
| [classmethod()](https://docs.python.org/3/library/functions.html#classmethod)  | [getattr()](https://docs.python.org/3/library/functions.html#getattr)          | [locals()](https://docs.python.org/3/library/functions.html#locals)         | [repr()](https://docs.python.org/3/library/functions.html#repr)                  | [zip()](https://docs.python.org/3/library/functions.html#zip)                   |
| [compile()](https://docs.python.org/3/library/functions.html#compile)          | [globals()](https://docs.python.org/3/library/functions.html#globals)          | [map()](https://docs.python.org/3/library/functions.html#map)               | [reversed()](https://docs.python.org/3/library/functions.html#reversed)          | [\__import__()](https://docs.python.org/3/library/functions.html#__import__)    |
| [complex()](https://docs.python.org/3/library/functions.html#complex)          | [hasattr()](https://docs.python.org/3/library/functions.html#hasattr)          | [max()](https://docs.python.org/3/library/functions.html#max)               | [round()](https://docs.python.org/3/library/functions.html#round)                |                                                                                 |

Dus weet je ook al hoe je ze gebruikt: Je roept ze aan met de naam van de
functie en geeft èèn (of meer) parameter(s) mee tussen haakjes.

Een functie is niets anders dan een blok code met een naam. Je kunt van elk blok
code een functie maken. (Al is dat niet altijd even zinvol.) Maar Python moet
natuurlijk wèl weten welke code een functie is, dus is er voor de definitie van
een functie een specifieke syntax. De functies in Python gedragen zich niet
anders dan de functies in javaScript, PHP, C, C++, Java. Als je in een andere
taal al functies hebt gebruikt, weet je al wat ze doen en hoe ze werken.

Hoe maak je een functie in Python?

def functienaam( parameters) :

code (zoveel regels code als nodig)

return [expression]

Een functie begint met het keyword def, dan volgt de naam van de functie,
gevolgd door “()”  
Tussen de haakjes staan eventuele parameters die je aan de functie meegeeft. De
functie gaat iets doen met die parameter(s), of voert er een bewerking op uit
die een resultaat produceert.

Het einde van de functie wordt gemarkeerd door “return” Dit is altijd het einde
van de functie. Je hebt al vaker gezien in Python dat een codeblokje
ingesprongen is. Zo markeert Python een code blokje: Een “:” aan het begin, dan
ingesprongen (indentated) regels code.

Op de laatste regel staat een return; met of zonder een expressie. Staat er wel
een expressie, dan is dit de waarde die door de functie wordt teruggegeven. Want
globaal zijn er twee soorten functies :

1. Er zijn functies die iets **doen**. Zoals de functie print().

2. Er zijn functies die data **bewerken** en het resultaat teruggeven, zoals de
    functie int().

Laten we maar eens een functie maken. In dit geval is het een functie die een
list in omgekeerde volgorde weergeeft.

We beginnen met de definitie van de functie. Onthoudt dat functies altijd aan
het begin van jouw programma gedefinieerd moeten worden.  
**Vraag**: Kun je bedenken waarom dat zo is?
zodat het weet dat het een function is
De code:

```python
def keerdelistom(x):

for i in reversed(x):

print(i, end= ' ')

print()

return

a = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]

keerdelistom(a)
```

We gebruiken hier trouwens nog een functie: reversed(). Deze is één van de
built-in functies van Python.  
**Vraag**: Leg uit wat reversed() precies doet.
het reversed de string 
## Opdracht

**Opdracht**: Maak een stukje code waarin:

Een omrekening plaatsvindt van gradencelcius naar gradenfahrenheit. Je geeft dus
aan de functie een temperatuur in graden celcius en je krijgt de temperatuur in
graden celcius terug\*.

- Een variabele (bijvoorbeeld gradencelcius) aan een functie wordt
    doorgegeven, waarbij de functie:

- Deze temperatuur in graden celcius omrekent naar graden fahrenheit.

- Het resultaat teruggeeft aan een andere variabele in de code (bijvoorbeeld
    gradenfahrenheit). Hier moet je de functie return gebruiken.

- Buiten de functie print je dan de oorspronkelijke variabele èn de waarde die
    de functie teruggeeft.

Let op: return is het laatste statement dat in de functie wordt uitgevoerd. Die
staat dus (bijna altijd) onderaan.

*\* De formule voor deze berekening kwam in de README van datatypes aan de
orde.*

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(str(celsius) + 'Celsius is: ' + str(fahrenheit)  + ' Fahrenheit')

### Leerdoelen

Eén of meerdere leerdoelen die het liefst SMART zijn geformuleerd en slaan op de
inhoud van deze taak.

Voorbeeld:

- Ik kan met Python een functie aanspreken

- Ik kan parameters doorgeven aan een functie

- Ik kan met Python een functie definiëren

- Ik weet dat er twee soorten functies te onderscheiden zijn

- Ik kan een functie iets laten uitvoeren

- Ik kan een functie het resultaat van een bewerking teruggeven

### Eindresultaat

Het eindresultaat is een regel tekst waarin iets staat als:

De temperatuur van 25 graden Celcius is 77 graden Fahrenheit

of: mooier(!)

25° Celcius komt overeen met 77° Fahrenheit.

### Bronnen

<https://www.tutorialspoint.com/python3/python_functions.htm>

<https://www.freecodecamp.org/news/python-return-statements-explained-what-they-are-and-why-you-use-them>

en voor wie de diepte in wil:

<https://docs.python.org/3/reference/compound_stmts.html#function-definitions>

en

<https://docs.python.org/3/reference/simple_stmts.html#the-return-statement>
