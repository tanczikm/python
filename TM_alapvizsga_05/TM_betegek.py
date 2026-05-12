class Beteg:
    def __init__(self,sorszam,nev,taj_szam):
        self.sorszam = sorszam
        self.nev = nev
        self.taj_szam = taj_szam
    
    def varakozas(self):
        return self.sorszam * 5

betegek = []



for sorszam in range(3):
    nev = input("Add meg a beteg nevét! ")
    taj_szam = input("Add meg a beteg TAJ számát! ")

    betegek.append([sorszam, nev, taj_szam, Beteg(sorszam, nev, taj_szam).varakozas()])


for beteg in betegek:
    print(f"{beteg[0]}. {beteg[1]} {beteg[2]}, Várható várakozás: {beteg[3]} perc.")