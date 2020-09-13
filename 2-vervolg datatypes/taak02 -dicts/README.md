# Python Basic -vervolg datatypes - Taak02 – Dict

## Dictionaries (dict)

**Wat zijn dictionaries?**

## Uitleg

Dictionaries in Python zijn wat in PHP associative arrays zijn.  
Er is dus ook altijd sprake van een tweetal: de key en de waarde van die key.

Dictionaries zijn veranderbaar. (mutable) dat betekent dat je de waarden te
allen tijden kunt veranderen.  
Dictionaries kun je groter en kleiner maken: Je een key – waarde combinaties
toevoegen en weghalen.

Een dictionary van enkele provincies van Nederland met de hoofdsteden ziet er zò
uit.

Je kunt verschillende notaties tegenkomen:

**Notatie 1:**

```python
Provinciehoofdsteden = dict([
('Noord_Holland' , 'Amsterdam'),
('Zuid_Holland', 'Den_Haag'),
('Utrecht', 'Utrecht'),
])
```

**Notatie 2:**

```python
Provinciehoofdsteden = dict(
Noord_Holland='Amsterdam',
Zuid_Holland='Den_Haag',
Utrecht='Utrecht',
)
```

Notatie 3:

```python
Provinciehoofdsteden = {
'Noord_Holland' : 'Amsterdam',
'Zuid_Holland' : 'Den_Haag',
'Utrecht' : 'Utrecht',
}
```

En je kunt combinaties maken waarin de key een string is en de waarde een getal.  
**Een voorbeeld van zo'n dictionary:**

```python
Dagen_in_maanden = dict([
('januari', 31),
('februari',28), # niet een schrikkeljaar dus.
('maart',31),
… enz ..
])
```

**Opgaven:**

1. Voeg een statement toe waarmee je het type van “Provinciehoofdsteden”
    uitprint.

2. Voeg een statement (1 regel) toe waarmee je de inhoud van deze dictionary
    uitprint.

3. Voeg nu aan de dictionary provinciehoofsteden 3 provincies toe. In eerste
    instantie doe je dat door een grotere dictionary te maken, zoals in het
    voorbeeld hierboven. Je voegt dan enkele regels toe aan deze code.

Om een element aan een dictionary toe te voegen gebruik je een statement als:

```python
Provinciehoofdsteden['Zeeland'] = 'Middelburg'
```

1. Voeg op deze manier nog drie provincies met hun hoofdsteden toe en print de
    dictionary nogmaals uit.

Het verwijderen van een element is natuurlijk ook mogelijk. Zoek dat maar eens
op. (een link naar een oplossing vind je bij bronnen, hieronder. Er zijn op deze
pagina nog meer handelingen te vinden. We raden je aan om ze allemaal eens toe
te passen op het voorbeeld hierboven.)

1. Voeg een statement toe waarin je één van de hoofdsteden wijzigt in iets
    anders.
Provinciehoofdsteden['Groningen'] = 'Niet Groningen'
## Leerdoelen

- Ik weet wat dictionaries zijn

- Ik kan een dictionary aanmaken (initialiseren)

- Ik kan een element toevoegen met een statement

- Ik kan een element verwijderen met een statement

- Ik kan een waarde van een element veranderen met een statement.

## Bronnen

<https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python>
