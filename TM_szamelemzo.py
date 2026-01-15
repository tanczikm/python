szamok = []

while True:
    szam = int(input("Kérek egy egész számot (0-val kilép): "))

    if szam == 0:
        print("Bemenet:", szamok)
        break

    else:
        szamok.append(szam)

pozitiv_szamok = 0
negativ_szamok = 0

paros_szamok = []
paratlan_szamok = []

min_szam = 1000000000000000
max_szam = -1000000000000000

for szam in szamok:
    if szam >= 0:
        pozitiv_szamok = pozitiv_szamok + szam
    if szam < 0:
        negativ_szamok = negativ_szamok + 1

    if szam % 2 == 0:
        paros_szamok.append(szam)
    if szam % 2 == 1:
        paratlan_szamok.append(szam)

    if szam < min_szam:
        min_szam = szam
    
    if szam > max_szam:
        max_szam = szam
    


    

print("Megadott számok száma:", len(szamok))

print("Pozitív számok összege:", pozitiv_szamok)
print("Negatív számok száma:", negativ_szamok)

print("Páros számok száma:", len(paros_szamok))
print("Páratlan számok száma:", len(paratlan_szamok))

print("Legnagyobb szám:", max_szam)
print("Legkisebb szám:", min_szam)
