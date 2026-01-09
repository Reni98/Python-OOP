class Autok:
    def __init__(self,marka,evjarat,szin):
        self.marka=marka
        self.evjarat=evjarat
        self.szin=szin

    def kiir(self):
        print(f"Márka:{self.marka},Evjárat:{self.evjarat},Szín:{self.szin}")

# auto1=Autok("Suzuki",2020,"fehér")
# auto2=Autok("Volvo",2015,"fekete")
# auto1.kiir()
# auto2.kiir()


class Dolgozok:
    def __init__(self,nev,szulev,beosztas,fizetes):
        self.nev=nev
        self.szulev=szulev
        self.beosztas=beosztas
        self.fizetes=fizetes

    def kiir(self):
        print(f"A dolgozó: {self.nev}, Születésiév:{self.szulev},Beosztás: {self.beosztas}, Fizetés:{self.fizetes}")

# dolgozo1=Dolgozok("John Doe", 2010, "Rendszergazda", 310000)
# dolgozo1.kiir()

#Hozzatok létre egy Allatok nevű osztályt,
#Tárolját el az állatok adatait: fajta, neve,szin,hang
#Írjátok ki a konzolra az adatokat.

class Allatok:
    def __init__(self,fajta,nev,szin,hang):
        self.fajta=fajta
        self.nev=nev
        self.szin=szin
        self.hang=hang

    def kiir(self):
        print(f"Az állat fajtája: {self.fajta},neve: {self.nev}, szín: {self.szin}, hang:{self.hang} ")

allat1=Allatok("kutya","Morzsi","fekete","ugat")
allat1.kiir()