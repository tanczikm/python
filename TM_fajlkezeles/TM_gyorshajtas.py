def leggyorsabb(autok):
    leggyorsabb_sebesseg = 0
    for auto in autok:
        if auto[2] > leggyorsabb_sebesseg:
            leggyorsabb_sebesseg = auto[2]
            leggyorsabb_rendszam = auto[0]
            leggyorsabb_tipus = auto[1]
        if auto[2] > 50:
            gyorshajtok.append(auto)
    return f"{leggyorsabb_rendszam}, {leggyorsabb_tipus}, {leggyorsabb_sebesseg} km/h"
            
print("1) Adatok beolvasása")
allomany = open("gyorshajtas.txt", "r", encoding="utf-8")
autok = []

for sor in allomany:
    sor = sor.strip()
    sor = sor.split(";")
    sor[2] = int(sor[2])

    autok.append(sor)

print(f"2) Autók száma: {len(autok)}.")


gyorshajtok = []


print(f"3) A leggyorsabb autó: {leggyorsabb(autok)}")

print(f"4) Az 50 km/h sebességet {len(gyorshajtok)}-en lépték át.")
print("5) Gyorshajtók listája:")
for auto in gyorshajtok:
    print(f"{auto[0]} {auto[1]}    {auto[2]} km/h")

allomany.close()