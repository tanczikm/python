from gyakorlo_3_18pont_v2 import csoki

celfajl = open("csokik.txt", "r", encoding="utf-8")
csokik = []

for sor in celfajl:
    fajta, tomeg, csomag = sor.strip().split(";")
    uj_csoki = csoki(fajta, int(tomeg), csomag)
    csokik.append(uj_csoki)    

celfajl.close()

feher_csokik = []
for cs in csokik:
    if cs.tipus == "fehér":
        feher_csokik.append(cs.tomeg)

if len(feher_csokik) > 0:
    fehercsoki_atlag = sum(feher_csokik) / len(feher_csokik)
    print(f"A fehér csokik átlagos tömege: {round(fehercsoki_atlag, 1)}g")
else:
    print("Nincs fehér csoki az adatok között.")

papir_db = 0
for cs in csokik:
    if cs.csomagolas == "papír":
        papir_db = papir_db + 1

print(f"Összesen {papir_db} papír csomagolású csoki van.")


tipus = input("Kérem, adja meg a csoki típusát: ")
tomeg = int(input("Kérem, adja meg a csoki tömegét: "))
csomag = input("Kérem, adja meg a csoki csomagolását: ")
mennyiseg = int(input("Kérem, adja meg hány adagot szeretne: "))

talalat = None
for cs in csokik:
    if cs.tipus == tipus and cs.tomeg and cs.csomagolas == csomag:
        talalat = cs
        break

if talalat is not None:
    osszar = talalat.ar() * mennyiseg
    print(f"A termék ({tipus}, {tomeg}g, {csomag} csomagolás, {mennyiseg} adag) ára: {osszar} Ft")
else:
    print("Hiánycikk.")