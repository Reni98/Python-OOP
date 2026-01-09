# Mi az osztály?
# Az osztály (class) egy sablon vagy tervrajz, amelyből objektumokat (példányokat) hozhatunk létre. Gondolj rá úgy, mint egy receptre: a recept leírja, hogyan készítsünk süteményt, de a recept önmagában nem ehető — csak a sütemény, amit belőle készítünk, az.

# Objektum: az osztály alapján létrehozott tényleges dolog (példány).

# Mire jó az osztály?

# Adat + viselkedés együtt: Egy osztály egyszerre tudja tárolni az adatokat (például egy autó színét, márkáját) és a hozzá tartozó műveleteket (például elindít, megáll).
# Újrahasználhatóság: Egy osztályból több objektumot is létrehozhatunk, mindegyik saját adatokkal rendelkezik.
# Rendszerezés: Segít a kódot logikusan és átláthatóan felépíteni.

# Kulcsfogalmak

# Osztály (class): a sablon, ami leírja az adatokat és a viselkedést.
# Objektum / példány (instance): az osztály alapján létrehozott tényleges "dolog".
# Attribútum (attribute): az objektumhoz tartozó adat (pl. név, életkor, szín).
# Metódus (method): az objektumhoz tartozó funkció vagy művelet (pl. elindít(), kiír()).
# Konstruktor (__init__): speciális metódus, amelyet az objektum létrehozásakor hívunk, és beállítja az attribútumokat.

class Autó:
    # Konstruktor: az attribútumok beállítása
    def __init__(self, márka, szín):
        self.márka = márka  # attribútum
        self.szín = szín    # attribútum

    # Metódus: viselkedés
    def bemutatkozik(self):
        print(f"Ez egy {self.szín} {self.márka}.")


auto1 = Autó("Toyota", "piros")  # objektum létrehozása
auto2 = Autó("Ford", "kék")

auto1.bemutatkozik()  # Ez egy piros Toyota.
auto2.bemutatkozik()  # Ez egy kék Ford.


class Dolgozo:
    def __init__(self, nev, kor, beosztas, fizetes):
        self.nev = nev
        self.kor = kor
        self.beosztas = beosztas
        self.fizetes = fizetes

    def fizetes_emeles(self, osszeg):
        self.fizetes += osszeg
        print(f"{self.nev} új fizetése: {self.fizetes}")

# Objektumok létrehozása
dolgozo1 = Dolgozo("Anna", 30, "Programozó", 500000)
dolgozo2 = Dolgozo("Béla", 40, "Projektvezető", 700000)

# Adatokhoz hozzáférés és műveletek
dolgozo1.fizetes_emeles(50000)  # Anna fizetését emeli
print(dolgozo2.beosztas)        # Kiírja Béla beosztását


# Az osztály tartalmazza az adatokat (attribútumokat) és a műveleteket (függvényeket).
# Az osztályban lévő függvényeket metódusoknak nevezzük, mert az adott osztályhoz/objektumhoz tartoznak.
# Ezekkel a metódusokkal tudjuk módosítani vagy használni az objektum adatait.

class BankSzamla:
    def __init__(self, tulajdonos, egyenleg):
        self.tulajdonos = tulajdonos
        self.egyenleg = egyenleg

    # Metódus: pénz befizetése
    def befizetes(self, osszeg):
        self.egyenleg += osszeg
        print(f"{self.tulajdonos} új egyenlege: {self.egyenleg} Ft")

    # Metódus: pénz kifizetése
    def kifizetes(self, osszeg):
        if osszeg <= self.egyenleg:
            self.egyenleg -= osszeg
            print(f"{self.tulajdonos} új egyenlege: {self.egyenleg} Ft")
        else:
            print("Nincs elég pénz!")

# Objektum létrehozása
szamla1 = BankSzamla("Anna", 100000)

# Metódusok használata
szamla1.befizetes(50000)  # növeli az egyenleget
szamla1.kifizetes(20000)  # csökkenti az egyenleget

# Az attribútumok = adatok (pl. tulajdonos, egyenleg)
# A metódusok = függvények az osztályon belül, amikkel dolgozunk az adatokkal (pl. befizetés, kifizetés)