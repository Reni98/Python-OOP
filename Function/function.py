# Függvény definíció

# „A függvény egy névvel ellátott kódrészlet, amely egy konkrét műveletet vagy számítást végez, és opcionálisan visszaadhat egy értéket, amit a program más részeiben újra felhasználhatunk.”

# Mire jó a függvény?

# Újrafelhasználás – egyszer írod meg, sokszor használhatod.
# Átláthatóság – a kód könnyebben érthető, kisebb részekre bontható.
# Adatátadás – paraméterek segítségével tudsz adatot adni a függvénynek.
# Eredmény visszaadása – return segítségével a függvény által kiszámolt érték tovább használható más kódrészletekben.


# Ez egy egyszerű függvény meghívás
# Nincs paraméterátadás
# A függvény csak egy utasítást hajt végre

# def koszon(): → függvény definiálása
# () → nincs paraméter
# koszon() → függvény meghívása
# print("Szia!") → a függvény törzse

def koszon():
    print("Szia!")
koszon()


# A függvénynek van egy paramétere, aminek a neve: nev.
# A függvény meghívásakor átadjuk az 'Anna' értéket a nev paraméternek.
# Kulcsfogalmak:
# paraméter → a függvény definíciójában van
# argumentum → a függvény meghívásakor adjuk át

def udvozol(nev):
    print("Szia", nev)
udvozol("Anna")


#Alapértelmezett paraméter
def udvozol1(nev="Diák"):
    print("Szia", nev)

udvozol1()        # Szia Diák
udvozol1("John")  # Szia John

#Lokális változó:
def pelda():
    x = 11  # csak a függvényen belül él
    print(x)

pelda()
# print(x)  #  hiba, kívülről nem látszik
# A lokális változó csak a függvényen belül él, amikor a függvény fut.
# Amint a függvény lefutott, a x törlődik a memóriából, kívülről nem férünk hozzá.


# Publikus függvény → bárki használhatja, az API része.
# Privát függvény → csak a belső működéshez, nem része a publikus felületnek.
# Pythonban a konvenció az _ használata, nem kötelező, de tisztább a kód.
def _belso_szamitas(a, b):
    return a + b

def osszead_kulso(a, b):
    return _belso_szamitas(a, b)

print(osszead_kulso(3, 4))  # 7
# _belso_szamitas(3, 4)  -> működik, de nem ajánlott
#A privát függvény csak belső használatra van, kívülről hívni nem ajánlott, mert a kód később megsérülhet, vagy nem lesz áttekinthető.”

#Példa: 
def _fizetes_szamitas(alapber, bonusz):
    # Privát: nem akarjuk, hogy bárki ezt közvetlenül hívja
    return alapber + bonusz

def fizetes_lekerdez(alapber, bonusz):
    # Publikus: ezt hívhatja a külső kód
    return _fizetes_szamitas(alapber, bonusz)

fizetes = fizetes_lekerdez(300000, 50000)
print(f" A fizetés: {fizetes}")
#Privát függvényt használunk, ha a működés részleteit el akarjuk rejteni, de az eredményt publikus módon szeretnénk elérhetővé tenni.


# def osszead(szam1,szam2):
    #Ez a függvény kiszámolja az összeget és kiírja, de nem tér vissza értékkel.
    # print(f"Eredmény: {szam1 + szam2}") None
    #return szam1 + szam2
# osszead(5,5)
#eredmeny = osszead(5,5)
#print(f"Eredmény: {eredmeny}")

# Ha egy függvénynek van visszatérési értéke, akkor az eredményét fel tudjuk használni másik függvényben vagy a program más részeiben.


# A lista feltöltő függvény visszaad egy listát, amit a főprogram eltárol.”

# „A kiíró függvény paraméterként kapja a listát, és kiírja az elemeit.”

# „A return-nel adjuk vissza az adatot, hogy tovább tudjuk használni.”

# „A while ciklus addig fut, amíg a felhasználó nem ad 0-t.”
def lista_feltolt():
    szamok=[]

    szamot_megad=True
    while szamot_megad:
        szam=int(input("Adj meg egy számot: "))
        if szam==0:
            szamot_megad= False
        else:
            szamok.append(szam)
    return szamok

def kiir(szamok):
    print("Szamok:")
    for sz in szamok:
        print(sz)

lista = lista_feltolt()
kiir(lista)

# lista_feltolt() → készít egy listát [10, 20, 30]
# lista = lista_feltolt() → a visszaadott listát elmentjük lista változóba
# kiir(lista) → átadjuk a listát a kiir függvénynek
# Vagyis a visszatérési értéket egy változóban tároljuk, és ezt a változót adjuk tovább paraméterként egy másik függvénynek.


#Fogalmak:
# | Fogalom                               | Mit jelent?                                                                                                    |
# | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
# | **Függvény (function)**               | Egy névvel ellátott kódrészlet, ami egy műveletet vagy számítást végez, és opcionálisan visszaad egy értéket.  |
# | **Függvény definíció (definition)**   | A `def` kulcsszóval létrehozott kódrészlet. Pl. `def koszon(): ...`                                            |
# | **Függvény meghívás (call)**          | Amikor használjuk a függvényt, pl. `koszon()`.                                                                 |
# | **Paraméter (parameter)**             | A függvény definíciójában szereplő változó, ami adatot vár. Pl. `nev` a `def udvozol(nev):`-ben.               |
# | **Argumentum (argument)**             | A függvény meghívásakor átadott tényleges adat. Pl. `udvozol("Anna")` → `"Anna"` az argumentum.                |
# | **Visszatérési érték (return value)** | A függvény által visszaadott érték, amit a program más részeiben felhasználhatunk. Pl. `return szam1 + szam2`. |

# | **Lokális változó (local variable)**              | A függvényen belül él, kívülről nem látható. Pl. `x = 10` a függvényen belül.                                   |
# | **Globális változó (global variable)**            | A program egészében látható változó, de használata kezdőknél kerülendő.                                         |
# | **Privát függvény / segédfüggvény**               | `_` jellel kezdődő függvény, belső használatra, kívülről nem ajánlott hívni.                                    |
# | **Publikus függvény**                             | Külső kód is hívhatja, a modul “API”-jának része.                                                               |
# | **Alapértelmezett paraméter (default parameter)** | Olyan paraméter, amihez a függvény definiálásakor adunk alapértelmezett értéket. Pl. `def udvozol(nev="Diák"):` |
# | **Dokumentációs string (docstring)**              | Rövid leírás a függvény működéséről, pl. `"""Ez a függvény összead két számot."""`                              |
