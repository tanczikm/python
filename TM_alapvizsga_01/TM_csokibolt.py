from gyakorlo_3_18pont_v2 import csoki

celfajl = open("csokik.txt", "r", encoding="utf-8")
fehercsoki_tomegek = []
papircsomagolasu = 0

for sor in celfajl:
    sor = sor.strip()
    sor = sor.split(";")
    
    if sor[0] == "fehér":
        fehercsoki_tomegek.append(int(sor[1]))
    if sor[2] == "papír":
        papircsomagolasu = papircsomagolasu + 1

celfajl.close()


fehercsoki_atlag = sum(fehercsoki_tomegek) / len(fehercsoki_tomegek)
print(f"A fehér csokik átlagos tömege: {round(fehercsoki_atlag, 1)}g")

print(f"Összesen {papircsomagolasu} papír csomagolású csoki van.")


csoki_tipus = input("Kérem, adja meg a csoki típusát: ")
csoki_tomeg = input("Kérem, adja meg a csoki tömegét: ")
csoki_csomagolas = input("Kérem, adja meg a csoki csomagolását: ")
csoki_adag = int(input("Kérem, adja meg hány adagot szeretne: "))

print(csoki.ar(csoki(csoki_tipus, csoki_tomeg, csoki_csomagolas)))