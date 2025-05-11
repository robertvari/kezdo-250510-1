## Adattípusok (data types)
```python
# string (str)
"Hello my name is Robert Vari."
'Hello my name is Kiss Csaba.'
"It's my birthday!"
'It\'s my birthday!'

# boolean (bool)
True, False

# Numbers
# integers (int)
1, 2, 100, 200, -1, -2, -100, -200

# float
3.14, -3.14

# lists
["Kriszta", "Csaba", "Tamás"]
[1, 2, 3, 4]

# dictionaries
{
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}
```

## String parancsok (string methods)
Néhány példa a string-ekkel gyakran használt parancsokról.

**upper()** Minden nagybetű.
```python 
print("Hello World!".upper())
```

**lower()** Minden kisbetű.
```python 
print("Hello World!".lower())
```

**title()** Minden kezdőbetű nagy.
```python
print("kiss csaba".title())
```

**replace("from", "to")** Keres és kicserél. Fontos, hogy itt meg kell adnod a parancs paramétereinél, hogy mit mire cseréljen!
```python
print("Hello World!".replace("World", "Csaba"))
```

**split()** Szétválasztja a mondatokat a ``space`` karakternél és visszakapsz egy listát.
```python
print("Hello World!".split())
>>>['Hello', 'World!']
```
A ```split()``` parancsnak megadhatsz egy karaktert vagy szót is amit a szétválasztáshoz használni akarsz. 
```python
print("Hello".split("e"))
>>>['H', 'llo']
```

## Változók (variables)
A változó egy adat tárolására szolgál. Lényegében adatot tárolsz a memóriában egy “cimke” (változó neve) segítségével. Amire figyelni kell változó névnél:
- A változó neve nem kezdődhet számmal
- Nem lehetnek ékezetes karakterek a névben
- Nem lehet ``space`` a névben

**Változó deklarálása**
```python
name = "Csaba"
address = "Pécs"
age = 26
```

Miután deklaráltál egy változót a benne tárolt értéket elő trudod hívni a print() paranccsal:
```python
print(name)
>>>Csaba
```
>**Fontos!**  
A változót mindig előbb deklaráljuk és csak utána használhatjuk!

A változókat egy sorban is deklarálhatod: 
```python
name, age, address = "Robert", 42, "Budapest"
```

## Változók felülírása (override variables)
Helyet spórolunk a memóriában ha az adatokat ugyanazon változónév alatt tároljuk a program futása alatt. Ilyenkor felülírjuk a korábban tárolt adatokat a változóban. 

```python
name = "Csaba"
print(f"Hello {name}!")

name = "Kriszta"
print(f"Hello {name}!")

name = "Tamás"
print(f"Hello {name}!")
```

A fenti példában látod, hogy mindig ugyanazt a változó nevet használtam a név tárolására. 

>**Fontos!**  
Figyelj arra, hogy ha tároltál egy adatot a változóban akkor használd is mielőtt felülírod egy másik adattal. 

## A formázott string (formated string)
Most hogy ismered a változókat használhatod a formázott string-et olyan mondatok kiírására melyben egyes szavak változókból jönnek. A formázott stringeket ``f`` karakterrel jelöljük a string előtt.

```python
name = "Csaba"
address = "Pécs"
age = 26

# f = formated string
print(f"Hello {name}. You live in {address}. You are {age} years old.")
```

## Listák (lists)
A listák olyan adattípusok amikben több adatot is tárolhatsz. A lista megnyitásáhot a ``[]`` karaktereket használjuk és az elemeket ``,`` választja el egymástól.
**Lista deklarálása**
```python
my_friends = ["Csaba", "Kriszta", "Tamás", "Aladár"]
```

**Elemek lekérése**  
Listák elemeit az indexük megadásával kérheted le. Az indexelés mindig 0-val indul.
```python
print(my_friends[1])
>>>Kriszta
```

Egy lista utolsó eleme mindig a -1. helyen áll.
```python
print(my_friends[-1])
```

**Új elem hozzáadása**  
Listához az ``append()`` segítségével adhatsz új elemeket. A parancs az új elemet a lista végéhez adja.
```python
my_friends.append("Johnie")
```

Ha fontos hova kerül az új elem használd az ``insert()`` parancsot.
```python
my_friends.insert(1, "Johnie")
```

**Egy elem cseréje**  
A következő művelettel kicseréljük a listában a második elemet (0-tól számolva).
```python
my_friends[1] = "Balázs"
```

**Elemek törlése**
```python
my_friends.remove("Balázs")
```

Törölhetsz elemet a ``del`` paranccsal is ahol egy elem index értékét kell megadnod.
```python
del my_friends[0]
```

Ha a törlést és az elem lekérését egyszerre akarod akkor használd a ``pop()`` parancsot. Az alábbi példa azt mutaja, hogy törlöm és egy időben tárolom is a törölt elemet a listában. Ezt a parancsot akkor használjuk ha további müveleteket akarunk végezni a törölt elemmel.
```python
friend = my_friends.pop(0)
```

## Lista rendezése (sorting)
Egy lista elemeit rendezhetjül a sort() paranccsal. Az alábbi példa ABC sorrendbe rendezi a listát.
```python
my_friends = ["Csaba", "Kriszta", "Tamás", "Aladár"]
my_friends.sort()
print(my_friends)
```
A parancsnak megadható paraméternként az, hogy fordítsa meg a rendezést.
```python
my_friends.sort(reverse=True)
```

## Slicing
Listákat és string-eket szeletelhetünk a ``[::]`` operátorral. A következőben néhány példa egy string szeletelésére.

Kérem a karaktereket 0-4 indexig:
```python
address = "Budapest"
print(address[0:4])
>>>Buda
```

Ha az elemek lekérését a 0 indextől indítod az első szám kihagyható.
```python
print(address[:4])
>>>Buda
```

Kérem az elemeket a 2. indextől.
```python
print(address[2:])
>>>dapest
```

Minden második elem:
```python
print(address[::2])
>>>Bdps
```

Lista sorrendjének megfordítása:
```python
print(address[::-1])
>>>tsepaduB
```

## Szótárak (dictionaries)
A dictionary-ban az elemek nem indexeken helyezkednek el, hanem egy un. kulcs, vagy keresőszó megadásával kerülnek be. 

```python
phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}
```
Láthatod hogy egy dictionary-ban minden elem egy un. ``key:value`` párt alkot.

>**Fontos!**  
Egy dictionary-ban nem lehet két egyforma kulcs mivel a kulcsokat a lekérdezéshez használjuk.

**Elemek lekérése**  
Egy dictionary-ból elemeket mindig a kulcs megadásával kérhetünk le.
```python
print(phonebook["06201235376"])
```

Ha a lekérés eredménye egy dictionary akkor beljebb is mehetünk egy újabb kulcs megadásával:
```python
print(phonebook["06201235376"]["name"])
```

**Elem hozzáadás**  
Egy új elem hozzáadásához mindössze annyit kell tenned hogy definiálsz egy új kulcsot.
```python
phonebook["06201239876"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}
```

**Elem szerkesztése**  
Az előzőhoz hasonló itt viszont meglévő külcshoz adunk új értéket.
```python
phonebook["06201235376"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}
phonebook["06201235376"]["address"] = "Budapest"
```

**Elem törlése**  
Itt használhatjuk a ``del`` parancsot.
```python
del phonebook["06201235376"]
```

## Kondíciók (if/else/elif)
A programozásban gyakran kell vizsgálnunk egy változó állapotát hogy eldöntsük a kód mely része fusson tovább. Így hozunk létre elágazásokat a kódban. 

```python
number = 10

if number < 10:
	print("number is less than 10")
else:
	print("number is greater than 10")
```

A kondíciós operátorok a következők:

| Operátor      | Jelentés |
| ----------- | ----------- |
| ==      | Egyenlő       |
| !=      | Nem egyenlő       |
| <      | Kissebb       |
| >      | Nagyobb       |
| <=      | Kissebb-Egyenlő       |
| >=      | Nagyobb-Egyenlő       |

A következő példa ezenkenk az operátoroknak a használatát mutatja be: 
```python
number = 10

if number == 10:
    print("The number is 10")

if number != 10:
    print("Number is not 10")

if number < 10:
    print("Number is less than 10")

if number > 10:
    print("Number is greater than 10")

if number <= 10:
    print("The number is 10 or less")

if number >= 10:
    print("The number is 10 or greater")
```

### and
Ez az egyszerű mechanizmus további kondíciók vizsgálatával bővíthető az ``and`` és ``or`` segítségével. A következő esetben a ``print`` csak akkor fut le, ha a számunk 5 és 10 között van:
```python
if number < 10 and number > 5:
	print("Number is between 5-10")
```
Az ``and`` használatával a kondíció mindkét oldalának igaznak kell lennie. 

### or
Az ``or`` esetében elég ha csak az egyik oldal igaz, a másik lehet hamis. A következő példában a ``print`` sor csak akkor fut le ha a szám kisebb 10-nél vagy nagyobb 20-nál. Bármelyik oldal igaz lehet.

```python
if number < 10 or number > 20:
    print("number less than 10 or greater than 20")
```

### elif 
Előfordulhat, hogy a kondíciós listát bővíteni akarod több feltétel megvizsgálásával. Ilyenkor használhatod az ``elif`` parancsot:

```python
if number < 10:
    print("number is less than 10")
elif number == 10:
    print("number is 10")
elif number == 20:
    print("number is 20")
elif number == 30:
    print("number is 30")
```
### match/casse
Az újabb python verziókban több állapot vizsgálatára használható a match/casse is:
```python
status = 200

match status:
    case 200:
        print("OK")
    case 300:
        print("Multiple Choices")
    case 400:
        print("Bad Request")
    case 500:
        print("Internal Server Error")
    case _:
        print("This status is not handled")
```

## Ciklusok
### A for loop
Mikor loop-ról beszélünk akkor egy lista elemein szeretnénk műveleteket végrehajtani. A következő példában egy számsor elemeit fogom printelni:

```python
numberList = range(10)

for i in numberList:
	print(i)
```

Figyeld meg, hogy a ``print`` parancs már egy sorral beljebb kezdődik. Ez a kód blokk, amely addig ismétlődik amíg van elem a listában. Ez a blokk lehet több soros is mint a következő példában:

```python
for i in numberList:
	multiplied = i*i
	divided = i/100.0
	print(multiplied, divided)
```

**continue**  
Bizonyos esetekben szükséges lehet,, hogy a loop futása alatt “skippelj” elemeket. Tegyük fel, hogy van egy listád egy könyvtár fájljairól de abban a könyvtárban téged csak a ``.txt`` kiterjesztésű fájlok érdekelnek. A ciklus futása alatt ezt könnyen megoldhatod a continue segítségével:

```python
for filename in fileList:
	if not i.endswith(".txt"): 
        continue
	print(i)
```

**break**  
A ``break`` segítségével kiléphetsz a ciklusból akkor is ha az még nem ért a lista végére. Az alábbi példában a ciklus addig fut amíg nem talál egy fájlt ``.txt`` kiterjesztéssel:

```python
for i in fileList:
    if i.endswith(".txt"): 
        break
```

**enumerate()**  
Az ``enumerate()`` parancs egy listát fogad és loop-ban használva egyszerre adja vissza a lista index és elem adatait. Nagyon jól használható counter helyett.

```python
names = ["robert", "tamas", "balazs", "kriszta"]

for index, name in enumerate(names):
	print(index, name)
```

**List Comprehension**  
Listák létrehozásánál gyakran van szükség valamilyen filter alkalmazására, vagy egyszerű műveletekre a lista elemeinél. Lássunk egy példát egy számlistára, ahol minden elemet szeretnék önmagával szorozni. 

Alapesetben ez így nézne ki:
```python
numberList = range(10)

numberList2 = []
for i in numberList:
	numberList2.append(i*i)
```

A List Comprehension lényegében egy for loop egyetlen sorban amivel egy új listát állíthatunk elő:
```python
numberList2 = [i*i for i in numberList]
```

Ebben a kifejezésben alkalmazhatsz kondíciót is az eredmény szűrésére. A következőben szeretnék egy listát a 2-vel osztható számokról.

```python
numberList2 [i for i in numberList if i%2 == 0]
```

 ### A while loop 
A ``while`` ciklus a ``for``-al ellentétben nem egy listán fut végig, hanem addig ismétel egy folyamatot amíg egy feltétel igaz. 

```python
number = 0

while number < 10:
	print(number)
	number += 1
```

Ne feledd a ``number`` változó értékét minden ciklusban növelni, különben a ``while`` végtelen ciklusban fut. A ``continue`` és ``break`` parancsok itt is ugyanúgy használhatók mint a ``for`` loop esetében.

## Fájlok írása és olvasása

A fájlok írásánál és olvasásánál az ``open()`` parancsot használjuk. Az ``open()`` két paramétert fogad. Az első paraméter mindig a fájl elérési útvonala (teljes, vagy relativ...), a második a mód (read, write) amelyben a fájlt meg akarjuk nyitni. A következő egy példa egy .txt fájl kiírására:
```python
myName = "robert"
f = open("myFile.txt", "w")
f.write(myName)
f.close()
```

Nagyon elterjedt és biztonságos,  hogy fájlokat a with blokkal használjuk, mivel itt nem kell foglalkoznunk a fájl lezárásával, ezt a with megteszi nekünk. Lássuk a fenti példát így:
```python
with open("myFile.txt", "w") as f:
	f.write(myName)
```

Fájl olvasása:
```python
with open("myFile.txt", "r") as f:
	print f.read()
```

## Adatok kiírása .json formátumba
A json (Java Script Object Notation) egy elterjedt formátum aminek segítságável hatékonyabban tárolhatunk adatokat fájlokban és ezeket a fájlokat visszaolvasva egyből dictionary-t kapunk amivel könnyű dolgozni.

Alább egy példa egy egyszerű dictionary kiírására .json formátumba:
```python
import json

user_data = {
    "name": "Kiss Csaba",
    "address": "Debrecen",
    "email": "csaba@gmail.com"
}

with open("user_data.json", "w") as f:
    json.dump(user_data, f)
```

A .json fájlokat így olvassok be:
```python
import json

with open("user_data.json") as f:
    user_data = json.load(f)

print(user_data["name"])
print(user_data["address"])
print(user_data["email"])
```


## Gyakorló feladatok
[Gyakorló feladatok megoldásokkal (angol)](https://www.w3schools.com/python/exercise.asp?filename=exercise_syntax1)