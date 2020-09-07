# Taak01 Vervolg datatypes

In deze taak komen meer geavanceerde datatypes aan de orde.

## Lijsten

Als je een reeks gegevens hebt, kun je die in Python opslaan in één variabele,
zoals deze:

```python
maanden =
[‘januari’,’februari’,’maart’,’april’,’mei’,’juni’,’july’,’augustus’,’september’,’oktober’,’november’,’december’]
```

**Vraag**: Van welk datatype zijn alle elementen van deze lijst?
Strings
**Vraag**: Welk antwoord zou len(maanden) geven?
12
Je kunt alle elementen van deze lijst adresseren met een index: maanden[0] geeft
het eerste element.

**Opgave**: zoals je ziet is één element van deze lijst verkeerd gespeld. Er
staat ‘july’ in plaats van ‘juli’. Schrijf een statement waardoor ‘july’
vervangen wordt door ‘juli’.
maanden[6] = 'juli'
**Opgave**: Maak nu een programmaatje waarin je de inhoud van de lijst maanden
print. Hierbij staat elk element op een eigen regel, zoals

januari

februari

… etc.

maanden = "januari\nfebruari\nmaart\napril\nmei\njuni\njuly\naugustus\nseptember\noktober\nnovember\ndecember"


**Opgave**: Maak een statement waarmee je de lengte van een element (zoals
‘februari’) uit de lijst print.

Nu print je de inhoud van de lijst maanden opnieuw, waarbij niet alleen de
inhoud van het element wordt gegeven, maar op dezelfde regel ook de lengte van
die string.  
Doe dat met een for loop “in range()” èn met een for loop “in maanden”. *Geheid
dat je een foutmelding krijgt bij een for loop “in maanden”. Kun je ontdekken
wat hier gebeurt?*

Overigens kan een reeks ook verschillende datatypes bevatten. Er kunnen
integers, floats, strings door elkaar heen staan.  


**Vraag:** Wat gebeurt er als we een lijst opnemen in een lijst?
