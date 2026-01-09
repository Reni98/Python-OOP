def udvozol(nev):
    print(f"Szia {nev}.")
udvozol("John")

def osszead(a,b):
    print(f"Összeadás: {a + b}" )
osszead(10,10)

def kivonas(c,d):
    return c-d
eredmeny=kivonas(10,8)

def kiir(kivon):
    print(f"Az eredmény: {kivon}")
kiir(eredmeny)

#Készítsetek szorzás függvényt és a szorzáskiir függvénnyel írjátok ki a szorzás eredményét

def szorzas(szam1,szam2):
    return szam1*szam2
sz=szorzas(5,5)

def szorzatkiir(szorzat):
    print(f"Szorzás eredménye: {szorzat}")
szorzatkiir(sz)

def listafeltolt():
    szamok=[]
    for i in range(5):
        szamok.append(i)
    return szamok
szamoklista=listafeltolt()

def listakiir(lista):
    for l in lista:
        print(l)
listakiir(szamoklista)

#Készítsetek kettő függvényt, az elsőnek a neve lfeltolt, a másodiknka lkiir, az első függvényben kérjetek be 3db számot és tároljátok el listában, a második függvényben írjátok ki a megadott számokat.

def lfeltolt():
    szamok=[]
    for i in range(3):
        szam=int(input("Adj meg egy számot:"))
        szamok.append(szam)
    return szamok
fmegad=lfeltolt()

def lkiir(ujlista):
    print("A felhasználó által megadott számok: ")
    for i in ujlista:
        print(i)
lkiir(fmegad)
